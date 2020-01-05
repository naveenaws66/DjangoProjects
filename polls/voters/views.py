from django.views.generic import ListView

#from django.http import HttpResponse

from .models import people

class VotersList(ListView):
    model = people
    template_name = 'voters/voters.html'
    context_object_name = 'all_voters'

