from django.urls import path, include
from rest_framework import routers
from rest_framework_test import views

route = routers.DefaultRouter()

# 注册新的路由地址
route.register('student', views.StudentViewSet)
route.register('activity', views.ActivityJoinViewSet)
route.register('user', views.StudentViewSet)
route.register('join_activity', views.StudentViewSet)


# 注册上一级的路由地址并添加
urlpatterns = [
    path('api/', include(route.urls)),
]