from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.response import Response

# Create your views here.

class HelloWordAPIView(views.APIView):
    def get(self, request):
        return Response({"message": "Hello, World! - from ContainTrack API - From Vercel"})