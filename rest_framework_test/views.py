from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Student, JoinActivity
from .serializers import StudentSerializers, ActivityJoinSerializers, ActivitySerializers, UserSerializers


# Create your views here.


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAuthenticated)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # 指定结果集并设置排序
    queryset = Student.objects.all().order_by('-pk')
    # 指定序列化的类
    serializer_class = StudentSerializers


class ActivityJoinViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = JoinActivity.objects.all().order_by('-pk')
    # 指定序列化的类
    serializer_class = ActivityJoinSerializers


class UserViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = JoinActivity.objects.all().order_by('-pk')
    # 指定序列化的类
    serializer_class = UserSerializers


class ActivityViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = JoinActivity.objects.all().order_by('-pk')
    # 指定序列化的类
    serializer_class = ActivitySerializers



