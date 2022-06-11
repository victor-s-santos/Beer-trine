from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.serializers import Serializer

class BeerListCreateView(generics.ListCreateAPIView):
    
    def get(self, request):
        return Response("Python")