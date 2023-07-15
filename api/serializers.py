from rest_framework import serializers
from .models import Benefit, Menu


class BenefitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Benefit
        fields = ('id', 'code',)


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'title',)
