from django.shortcuts import render
from personas.models import Persona


def home(request):

    personas = Persona.objects.order_by('id')

    dict_personas = {'personas': personas}

    return render(request, 'index.html', dict_personas)
