from django.shortcuts import render
from .models import Conference
from django.views.generic import ListView,DetailView
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