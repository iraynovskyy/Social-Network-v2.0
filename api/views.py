from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import auth  #, User
# from account.models import Account
from django.contrib import messages
# from .models import Post, Preference

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# from .serializers import PostSerializer
from datetime import datetime


# Create your views here.
@api_view(["GET"])
def welcome(request):
    content = {'Message': 'Welcome! It is a Home page!'}
    return JsonResponse(content)