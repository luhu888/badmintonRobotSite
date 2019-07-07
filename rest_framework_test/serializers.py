# -*- coding: utf-8 -*-
# __author__=luhu
from django_filters import rest_framework as filters
from rest_framework import serializers
from .models import Student, JoinActivity, Activity, User


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student  # 指定的模型类

        fields = ('pk', 'name', 'sex', 'sid')    # 需要序列化的属性


class ActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('activity_time', 'activity_place', 'activity_number')


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'user_id', 'password')


class ActivityJoinSerializers(serializers.ModelSerializer):
    class Meta:
        model = JoinActivity
        fields = ('activity_number', 'user_id')







