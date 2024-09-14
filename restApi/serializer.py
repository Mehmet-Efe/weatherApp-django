from rest_framework import serializers
from web.models import hava, searchForCity

class havaSerializer(serializers.ModelSerializer):
    class Meta:
        model = hava
        fields = '__all__'
        

class schedulerChange(serializers.ModelSerializer):
    class Meta:
        model = searchForCity
        fields = '__all__'
    