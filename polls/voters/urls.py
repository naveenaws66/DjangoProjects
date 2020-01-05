from django.urls import path

from .views import VotersList

urlpatterns = [
    path('', VotersList.as_view(), name='voterslist'),
]