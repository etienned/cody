# -*- coding: utf-8 -*-

from rest_framework import serializers

from voiture.models import Voiture


class VoitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voiture
        fields = (
            'id',
            'marque',
            'annee',
            'description',
            'cylindree',
            'proprietaire',
            'photo'
        )
