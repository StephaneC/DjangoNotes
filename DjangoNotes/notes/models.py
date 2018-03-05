# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.
class Note(models.Model):
    note = models.TextField()
    done = models.BooleanField(default=False)
    author = models.TextField(default='Anonymous')
    #def __init__(self, author, note, done=False):
    #    self.author = author
    #    self.note = note
    #    self.done = done

    def __init__(self, note):
        self.note = note
        self.done = False
        self.author = "Anonymous"
        self.date = datetime.now()