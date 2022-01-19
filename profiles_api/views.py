from operator import imod
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class helloApiView(APIView):
    """Test APIView"""

    serializer_class=serializers.HelloSerializers   
    def get(self,request,format=None):
        """Returns a list of APIView Features"""

        an_apiview=[
        'Uses HTTP Menthofs as functiosn (get, post, patch)',
        'Is similar to a tradational Django view'
        'Gives you the most control over application logic',
        'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self, request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get("name")
            message=f'Hello { name }'
            return Response({'message':message})
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                 )


    def put(self,request, pk=None):
        """Handle updating and object"""

        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle the partial update"""

        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete and object"""
        return Response({"method":"Delete"})