from django.urls import path
from . import views


app_name = 'conferenceapp'

urlpatterns = [
    # path('liste/', views.all_conferences, name='conference_list'),
    path("liste/", views.ConferenceList.as_view(), name="conference_list"),
    path("details/<int:pk>/", views.ConferenceDetail.as_view(), name="conference_detail"),
]