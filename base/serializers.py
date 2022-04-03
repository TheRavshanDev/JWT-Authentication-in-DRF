from audioop import mul
from rest_framework.serializers import ModelSerializer
from .models import Talks, Maqola, Muallif

class MuallifSerializer(ModelSerializer):
    class Meta:
        model = Muallif
        fields = '__all__'

class MaqolaSerializer(ModelSerializer):
    class Meta:
        model = Maqola
        fields = '__all__'

class TalksSerializer(ModelSerializer):
    class Meta:
        model = Talks
        fields = '__all__'