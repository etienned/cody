# -*- coding: utf-8 -*-

from rest_framework import generics

from voiture.models import Voiture
from voiture.serializers import VoitureSerializer


class VoitureList(generics.ListCreateAPIView):
    queryset = Voiture.objects.all()
    serializer_class = VoitureSerializer


class VoitureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Voiture.objects.all()
    serializer_class = VoitureSerializer
