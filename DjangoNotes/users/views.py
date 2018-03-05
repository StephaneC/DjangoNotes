# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from models import User
from serializers import UserSerializer

# Create your views here.
class UsersList(generics.ListCreateAPIView):
    """
    API endpoint that allows note to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date')
    serializer_class = UserSerializer
