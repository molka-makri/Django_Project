from django.urls import path
from . import views


app_name = 'conferenceapp'

urlpatterns = [
    # URLs pour les conférences
    # path('liste/', views.all_conferences, name='conference_list'),
    path("liste/", views.ConferenceList.as_view(), name="conference_list"),
    path("details/<int:pk>/", views.ConferenceDetail.as_view(), name="conference_detail"),
    path("form/", views.ConferenceCreateView.as_view(), name="conference_add"),
    path("<int:pk>/edit/", views.ConferenceUpdateView.as_view(), name="conference_edit"),
    path("<int:pk>/delete/", views.ConferenceDeleteView.as_view(), name="conference_delete"),
    
    # URLs pour les soumissions (ordre important : spécifique avant générique)
    path("submissions/", views.SubmissionListView.as_view(), name="submission_list"),
    path("submissions/add/", views.SubmissionCreateView.as_view(), name="submission_add"),
    path("submissions/<str:submission_id>/edit/", views.SubmissionUpdateView.as_view(), name="submission_edit"),
    path("submissions/<str:submission_id>/", views.SubmissionDetailView.as_view(), name="submission_detail"),
    path("submissions/<str:submission_id>/download/", views.download_paper, name="download_paper"),
]