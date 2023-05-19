from django.shortcuts import render
from rest_framework import viewsets
from .models import empleado 
from .serializers import empleadoserializers
# Create your views here.


class empleadoViewSet(viewsets.ModelViewSet):
    serializer_class = empleadoserializers
    queryset = empleado.objects.all()