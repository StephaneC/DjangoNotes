# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core import serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from models import User, Token
from rest_framework import generics, status
from serializers import UserSerializer
from DjangoNotes.custumauthentication import CustumAuthentication
import redis
import json


import logging
#import pdb; pdb.set_trace()

r = redis.StrictRedis(host='localhost', port=6379, db=0)

# store authenticated token 
REDIS_TOKEN = 'token_'
# store list of users
REDIS_USERS = 'users'
# Store token to be able to search for one simply
REDIS_USER = 'user_'



@api_view(['GET', 'POST', 'PUT'])
@authentication_classes((CustumAuthentication,))
def user_list_api(request):
    """
    GET : List all code users
    PUT : create a new user.
    POST : Authenticate user and give back Authentication token.
    """
    if request.method == 'GET':
        if request.user is None:
            return Response('unauthenticated', status=status.HTTP_401_UNAUTHORIZED)
        users = r.lrange('users', 0, 100)
        decoded = []
        if(len(users) >0):
            for n in users:
                decoded.append(json.loads(n))
                        
        serializer = UserSerializer(decoded, many=True)
        #if(serializer.is_valid()):
        return Response(serializer.data)
        #return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        # Authentication
        serializer = UserSerializer(data=request.data, context={'request': request, 'user': request.user})
        if serializer.is_valid():
            # Check the user exist in Redis
            found = r.get(REDIS_USER+serializer.data['username'])            
            # Check the pwd is correct
            if found is None:
                return Response('user or pwd incorrect', status=status.HTTP_401_UNAUTHORIZED)
            elif json.loads(found)['pwd'] != serializer.data['pwd']:
                # pwd incorrect
                return Response('user or pwd incorrect', status=status.HTTP_401_UNAUTHORIZED)

            # create token, store and send it back
            token = Token()
            r.setex(REDIS_TOKEN+token.token, token.duration, found)
            # s = TokenSerializer(data=token)
            #json = serializers.serialize('json', serializer.data)
            # Generate a token and store it to redis associate with user
            return Response(json.dumps(vars(token)), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = UserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            # check exist
            found = r.get(REDIS_USER+serializer.data['username'])            
            if found is not None:
                return Response('user already exist', status=status.HTTP_401_UNAUTHORIZED)

            # create user in redis
            r.set(REDIS_USER+serializer.data['username'], json.dumps(serializer.data))

            # Add user to users list in redis
            r.lpush(REDIS_USERS, json.dumps(serializer.data))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)