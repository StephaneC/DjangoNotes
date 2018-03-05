# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import Note
from session import Session
from rest_framework import generics, status
from serializers import NoteInputSerializer, NoteOutputSerializer

import logging
#import pdb; pdb.set_trace()

@api_view(['GET', 'POST'])
def notes_list_api(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        notes = Session().get()
        serializer = NoteInputSerializer(notes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NoteInputSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            logging.warning('serializer:%s', serializer.data) 
            Session().add(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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