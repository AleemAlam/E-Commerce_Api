from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Rating, Item
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import ItemSerializer, RatingSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(item__rating__gte = 4 )
    serializer_class = ItemSerializer
    permission_classes = (AllowAny,)
    

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.filter()
    serializer_class = RatingSerializer
    permission_classes = (AllowAny,)