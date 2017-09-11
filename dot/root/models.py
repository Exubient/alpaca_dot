import re
from django.db import models
from django.forms import ValidationError

TYPE_CHOICES = (
    ('o','organization'),
    ('v','volunteer'),
)

class Member(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    phone = models.IntegerField(max_length=12)
    email = models.EmailField()
   # Type = models.ChoiceField(choices = TYPE_CHOICES) #type은 예약어같음

class Post(models.Model):
    org_id = models.ForeignKey(Member)
    title = models.CharField(max_length=20)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class Matching(models.Model):
    vol_id = models.ForeignKey(Post,to_field="org_id")
    org_id = models.ForeignKey(Member) # 이렇게 하는게 맞나싶음..
    state = models.CharField()


class Comment(models.Model):
    post_id = models.ForeignKey(Post)
    vol_id = models.ForeignKey(Member)
    org_id = models.ForeignKey(Member)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)