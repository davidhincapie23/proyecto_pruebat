from rest_framework import serializers
from .models import empleado 


class empleadoserializers(serializers.ModelSerializer):
    class Meta:
        model = empleado
        fields = '__all__'