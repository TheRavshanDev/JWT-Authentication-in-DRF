from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from base.serializers import MaqolaSerializer, MuallifSerializer, TalksSerializer
from .models import Muallif, Talks, Maqola
from rest_framework.generics import ListAPIView

class MuallifViewSet(ListAPIView):
    queryset = Muallif.objects.all()
    serializer_class = MuallifSerializer
    permission_classes = [IsAuthenticated,]

class TalksViewSet(ModelViewSet):
    queryset = Talks.objects.all()
    serializer_class = TalksSerializer
    permission_classes = [IsAuthenticated,]

class MaqolaViewSet(ModelViewSet):
    queryset = Maqola.objects.all()
    serializer_class = MaqolaSerializer
    permission_classes = [IsAuthenticated,]
