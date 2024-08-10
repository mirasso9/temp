
from django.db import models

class DataState(models.Model):
    state = models.CharField(max_length=50, default='آنلاین✅')
    typing = models.CharField(max_length=50, default='خاموش❌')
    ans_pv = models.CharField(max_length=50, default='خاموش❌')
    join = models.CharField(max_length=50, default='خاموش❌')
    save = models.CharField(max_length=50, default='خاموش❌')
    join_save = models.CharField(max_length=50, default='خاموش❌')
    ans_gp = models.CharField(max_length=50, default='خاموش❌')
    read = models.CharField(max_length=50, default='خاموش❌')

class Word(models.Model):
    word = models.CharField(max_length=255)

