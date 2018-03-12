# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core import serializers
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from models import Note
from session import Session
from rest_framework import generics, status
from serializers import NoteInputSerializer, NoteOutputSerializer
import redis
import json
from DjangoNotes.custumauthentication import CustumAuthentication


import logging
#import pdb; pdb.set_trace()

r = redis.StrictRedis(host='localhost', port=6379, db=0)

@api_view(['GET', 'POST'])
@authentication_classes((CustumAuthentication,))
def notes_list_api(request):
    if request.user is None:
        return Response('unauthenticated', status=status.HTTP_401_UNAUTHORIZED)

    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        notes = r.lrange('notes', 0, 100)
        decoded = []
        if(len(notes) >0):
            for n in notes:
                decoded.append(json.loads(n))
                        
        serializer = NoteOutputSerializer(decoded, many=True)
        #if(serializer.is_valid()):
        return Response(serializer.data)
        #return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        serializer = NoteInputSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            logging.warning('serializer:%s', serializer.data) 
            #json = serializers.serialize('json', serializer.data)
            r.lpush('notes', json.dumps(serializer.data))
            Session().add(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes((CustumAuthentication))
@api_view(['GET', 'PUT', 'DELETE'])
def notes_api(request):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Note.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)