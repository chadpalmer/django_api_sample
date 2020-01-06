from rest_framework import serializers
from axioms.models import Axiom


class AxiomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Axiom
        fields = ('id', 'created', 'category', 'text', 'owner')
