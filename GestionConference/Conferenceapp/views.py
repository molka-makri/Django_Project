from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import ConferenceForm, SubmissionForm, SubmissionUpdateForm
from .models import Conference, Submission
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, FileResponse, Http404
from django.core.exceptions import PermissionDenied
# Create your views here.
# fonctions
def all_conferences(request): 
    conferences = Conference.objects.all()
    return render(request, 'conferences/list.html', {'conferences': conferences})
# classes
class ConferenceList(ListView):
    model = Conference
    template_name = 'conferences/list.html'
    context_object_name = 'conferences'
    ordering = ['start_date']

class ConferenceDetail(DetailView):
    model = Conference
    template_name = 'conferences/detail.html'
    context_object_name = 'conference'

class ConferenceCreateView(LoginRequiredMixin, CreateView):
    model = Conference
    form_class = ConferenceForm
    template_name = 'conferences/conference_form.html'
    success_url = reverse_lazy('conferenceapp:conference_list')

class ConferenceUpdateView(LoginRequiredMixin, UpdateView):
    model = Conference
    form_class = ConferenceForm
    template_name = 'conferences/conference_form.html'
    success_url = reverse_lazy('conferenceapp:conference_list')

class ConferenceDeleteView(LoginRequiredMixin, DeleteView):
    model = Conference
    template_name = 'conferences/conference_confirm_delete.html'
    success_url = reverse_lazy('conferenceapp:conference_list')


# ==================== VUES POUR LES SOUMISSIONS ====================

class SubmissionListView(LoginRequiredMixin, ListView):
    """Vue pour afficher la liste des soumissions de l'utilisateur connecté"""
    model = Submission
    template_name = 'submissions/list.html'
    context_object_name = 'submissions'
    paginate_by = 10

    def get_queryset(self):
        """Retourner seulement les soumissions de l'utilisateur connecté"""
        return Submission.objects.filter(user_id=self.request.user).select_related('conference_id').order_by('-submission_date')


class SubmissionDetailView(LoginRequiredMixin, DetailView):
    """Vue pour afficher le détail d'une soumission"""
    model = Submission
    template_name = 'submissions/detail.html'
    context_object_name = 'submission'
    pk_url_kwarg = 'submission_id'
    
    def get_object(self, queryset=None):
        """S'assurer que l'utilisateur ne peut voir que ses propres soumissions"""
        obj = get_object_or_404(Submission, submission_id=self.kwargs['submission_id'])
        if obj.user_id != self.request.user:
            raise PermissionDenied("Vous n'avez pas le droit d'accéder à cette soumission.")
        return obj


class SubmissionCreateView(LoginRequiredMixin, CreateView):
    """Vue pour créer une nouvelle soumission"""
    model = Submission
    form_class = SubmissionForm
    template_name = 'submissions/form.html'
    
    def form_valid(self, form):
        """Assigner l'utilisateur connecté à la soumission"""
        form.instance.user_id = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        """Rediriger vers la liste des soumissions après création"""
        return reverse_lazy('conferenceapp:submission_list')


class SubmissionUpdateView(LoginRequiredMixin, UpdateView):
    """Vue pour modifier une soumission existante"""
    model = Submission
    form_class = SubmissionUpdateForm
    template_name = 'submissions/update.html'
    pk_url_kwarg = 'submission_id'
    
    def get_object(self, queryset=None):
        """S'assurer que l'utilisateur ne peut modifier que ses propres soumissions"""
        obj = get_object_or_404(Submission, submission_id=self.kwargs['submission_id'])
        if obj.user_id != self.request.user:
            raise PermissionDenied("Vous n'avez pas le droit de modifier cette soumission.")
        
        # Vérifier que la soumission peut être modifiée
        if obj.status in ['accepted', 'rejected']:
            raise PermissionDenied(
                f"Cette soumission ne peut pas être modifiée car elle a été {obj.get_status_display().lower()}."
            )
        
        return obj
    
    def get_form(self, form_class=None):
        """Personnaliser le formulaire pour exclure certains champs"""
        form = super().get_form(form_class)
        # Les champs non modifiables sont automatiquement exclus du formulaire
        # car ils ne sont pas dans les fields du SubmissionForm
        return form
    
    def form_valid(self, form):
        """Traitement du formulaire valide"""
        # L'utilisateur et la date de soumission ne changent pas
        # Seuls title, abstract, keyword et paper peuvent être modifiés
        return super().form_valid(form)
    
    def get_success_url(self):
        """Rediriger vers la liste des soumissions après modification"""
        return reverse_lazy('conferenceapp:submission_list')
    
    def get_context_data(self, **kwargs):
        """Ajouter des informations contextuelles"""
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Modifier la soumission'
        context['submit_button_text'] = 'Sauvegarder les modifications'
        return context


def download_paper(request, submission_id):
    """Vue pour télécharger le fichier PDF d'une soumission"""
    submission = get_object_or_404(Submission, submission_id=submission_id)
    
    # Vérifier que l'utilisateur a le droit de télécharger
    if submission.user_id != request.user:
        raise PermissionDenied("Vous n'avez pas le droit de télécharger ce fichier.")
    
    if submission.paper:
        return FileResponse(
            submission.paper.open('rb'),
            as_attachment=True,
            filename=f"{submission.title}_{submission.submission_id}.pdf"
        )
    else:
        raise Http404("Fichier non trouvé")

