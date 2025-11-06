from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin:login')  # Rediriger vers la page de login admin
    else:
        form = CustomUserCreationForm()

    return render(request, 'userapp/register.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('userapp:login')  # Rediriger vers la page de login après la déconnexion