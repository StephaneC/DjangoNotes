# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    def __init__(self, username, date, urlPhoto):
        self.username = username
        self.date = created or datetime.now()
        self.urlPhoto = urlPhoto