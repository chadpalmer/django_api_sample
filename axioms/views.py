from django.shortcuts import render
from rest_framework import generics
from axioms.models import Axiom, Intro
from axioms.serializers import AxiomSerializer


class AxiomList(generics.ListCreateAPIView):
    queryset = Axiom.objects.all()
    serializer_class = AxiomSerializer


class AxiomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Axiom.objects.all()
    serializer_class = AxiomSerializer


def index(request):
    intro_object = Intro.objects.get(pk=1)
    axiom_objects = Axiom.objects.all()
    intro_object.num_axioms = len(axiom_objects)
    context = {'intro_object': intro_object}
    return render(request, 'axioms/index.html', context)
