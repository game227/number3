from django.shortcuts import render
from .models import Mamlakat
from .serializers import Mamlakat, MamlakatSerializer
from rest_framework import viewsets

# Create your views here.
class MamlakatViewSet(viewsets.ModelViewSet):
    queryset = Mamlakat.objects.all()
    serializer_class = MamlakatSerializer