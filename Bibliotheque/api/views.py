from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
#from django_filters import rest_framework as filters
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly

from .models import *
from .serializers import *

class TokenPairView(TokenObtainPairView):
    serializer_class = TokenPairSerializer


class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class LecteurViewSet(viewsets.ModelViewSet):
    queryset = Lecteur.objects.all()
    serializer_class = LecteurSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class RetraitViewSet(viewsets.ModelViewSet):
    queryset = Retrait.objects.all()
    serializer_class = RetraitSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class RemiseViewSet(viewsets.ModelViewSet):
    queryset = Remise.objects.all()
    serializer_class = RemiseSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]           

