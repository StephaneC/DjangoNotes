# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import time
import uuid

# Create your models here.
class User(models.Model):
    def __init__(self, username, urlPhoto, password, created=time.time()):
        self.username = username
        self.date = created
        self.urlPhoto = urlPhoto
        self.pwd = password

class Token(models.Model):
    def __init__(self):
        self.token = str(uuid.uuid4())
        # 3hours 
        self.duration = 3*60*60
        self.date = time.time()