from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import React
from .serializers import ReactSerializer
from rest_framework.decorators import api_view

# Create your views here.

class ReactCreateAPIView (generics.ListCreateAPIView):
    queryset = React.objects.all()
    serializer_class = ReactSerializer
    
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        school=serializer.validated_data.get('school')
        message=serializer.validated_data.get('message')
        
        serializer.save()
        
    @api_view(["POST"])
    def api_home(request,*args,**kwargs):
        serializer=ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.data)
            return Response(serializer.data)
        return Response({"invalid":"invalid data"},status=400)