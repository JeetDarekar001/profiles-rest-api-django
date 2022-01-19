from operator import imod
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class helloApiView(APIView):
    """Test APIView"""

    def get(self,request,format=None):
        """Returns a list of APIView Features"""

        an_apiview=[
        'Uses HTTP Menthofs as functiosn (get, post, patch)',
        'Is similar to a tradational Django view'
        'Gives you the most control over application logic',
        'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})
