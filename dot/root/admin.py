from django.contrib import admin
from .models import Member, Post, Matching, Comment


# Register your models here.

admin.site.register(Member)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','author','created_at', 'updated_at']


    #content_size.allow_tages = True #deprecated

admin.site.register(Post,PostAdmin)
admin.site.register(Matching)
admin.site.register(Comment)
