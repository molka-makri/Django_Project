from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

class RegisterView(CreateView):
    """Vue basée sur une classe pour l'inscription"""
    form_class = CustomUserCreationForm
    template_name = 'userapp/register.html'
    success_url = reverse_lazy('userapp:login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Votre compte a été créé avec succès! Vous pouvez maintenant vous connecter.')
        return response

@csrf_protect
@never_cache
def register(request):
    """Vue fonction pour l'inscription (alternative)"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Votre compte a été créé avec succès! Vous pouvez maintenant vous connecter.')
            return redirect('userapp:login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'userapp/register.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('userapp:login')  # Rediriger vers la page de login après la déconnexion