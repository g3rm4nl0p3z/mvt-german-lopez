from django.shortcuts import render
from personas.models import Persona


def crear_familiar(request, nombre, apellido, edad, email):

    persona = Persona(nombre=nombre, apellido=apellido, edad=edad, email=email)

    persona.save()

    dict_persona = {'persona': persona}

    return render(request, 'crear-familiar.html', dict_persona)


def crear_familiares(request):

    persona_1 = Persona(nombre='Juan', apellido='Perez', edad=21, email='jperez@mail.com')

    persona_2 = Persona(nombre='María', apellido='Juarez', edad=22, email='mjuarez@mail.com')

    persona_3 = Persona(nombre='Marcelo', apellido='Jaime', edad=23, email='mjaime@mail.com')

    personas = []

    personas.append(persona_1)

    personas.append(persona_2)

    personas.append(persona_3)

    persona_1.save()    # Crear y guardar familiares en forma masiva

    persona_2.save()

    persona_3.save()

    dict_personas = {'personas': personas}  # Listar familiares en forma masiva

    return render(request, 'crear-familiares.html', dict_personas)
