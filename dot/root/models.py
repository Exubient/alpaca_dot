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
    m_Type = models.ChoiceField(choices = TYPE_CHOICES)
    matching_set = models.ManyToManyField('Matching')

class Post(models.Model):
    org = models.ForeignKey(Member)
    title = models.CharField(max_length=20)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class Matching(models.Model):
    vol = models.ForeignKey(Post,to_field="org_id")
    org = models.ForeignKey(Member) # 이렇게 하는게 맞나싶음..
    post = models.ForeignKey(Post) # 어떤 포스트에대해서 무슨관계인지 알기위해선 추가하는게 좋을듯
    state = models.CharField()


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(Member) #org와 vol을 굳이 나눌 필요 없어보임.
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)