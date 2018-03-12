from rest_framework import serializers
from models import Note

import logging
'''
 Serializer for input. As input, user only post note message. 
 Date, author and done fields will be added automatically.
'''
class NoteInputSerializer(serializers.BaseSerializer):
    class Meta:
        model = Note
        fields = ('note',)

    def create(self, validated_data):
        return Note.objects.create(**validated_data)
    
    def to_representation(self, obj):
        return {
            'author': obj.author,
            'note': obj.note, 
            'done': obj.done,
            'date':obj.date
        }

    def to_internal_value(self, validated_data):
        logging.debug('create note')
        note = Note(
            note=validated_data.get('note'),
            user=self.context.get('request').user
        )
        return note

class NoteOutputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

    def to_representation(self, obj):
        return {
            'author': obj['author'],
            'note': obj['note'], 
            'done': obj['done'],
            'date': obj['date']
        }
