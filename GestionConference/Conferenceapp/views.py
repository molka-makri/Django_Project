from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ConferenceForm
from .models import Conference
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
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

