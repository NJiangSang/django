# -*- encoding: utf-8 -*-
"""
@File    : serializers.py
@Time    : 2022/12/7 11:07 AM
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""
from .models import Project
from rest_framework import serializers


# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = "__all__"

# 下面的部分和上面的等价，ModelSerializer可以替代与model中重复的代码，并包含了create和update方法。如果我们需要自定义，则重写这两个方法
class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    create_time = serializers.DateTimeField()
    update_time = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create and return a new `project` instance, given the validated data.
        """
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `project` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.create_time = validated_data.get('create_time', instance.create_time)
        instance.update_time = validated_data.get('update_time', instance.update_time)
        instance.save()
        return instance

