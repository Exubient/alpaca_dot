import re
from django.db import models
from django.forms import ValidationError



class Member(models.Model):
    TYPE_CHOICES = (
    ('o','organization'),
    ('v','volunteer'),
)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField()
    m_type = models.CharField(max_length=1, choices = TYPE_CHOICES)
    Post_set = models.ManyToManyField('Post')
    matching_set = models.ManyToManyField('Matching')

class Post(models.Model):
    org = models.ForeignKey(Member,unique=True)
    title = models.CharField(max_length=20)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class Matching(models.Model):
    vol = models.ForeignKey(Member,related_name='Machng_vol')
    org = models.ForeignKey(Post, to_field="org_id", related_name='Maching_org') # 이렇게 하는게 맞나싶음..
    post = models.ForeignKey(Post,) # 어떤 포스트에대해서 무슨관계인지 알기위해선 추가하는게 좋을듯
    state = models.CharField(max_length=20)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(Member) #org와 vol을 굳이 나눌 필요 없어보임.
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)