# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Table board
class Board(models.Model):
    # CharField设置max_length的原因有两个：1. 告诉数据库该字段的最大长度, 2. 校验用户的输入
    # unique表示该字段的数据不可重复
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Table topic
# board : topic == 1 : 0...n
# topic : board == 1 : 1
class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_update = models.DateTimeField(auto_now_add=True)   # 该参数告诉Django创建Topic对象的时候，自动创建该字段的值
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="topics")   # Django会默认创建一个关系名(class_name)_set,即 topic_set，此处重命名为topic
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="topics")


# Table post
class Post(models.Model):
    message = models.CharField(max_length=4000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+') #This instructs Django that we don’t need this reverse relationship, so it will ignore it.

# Table user is defined at django.contrib.auth.models
