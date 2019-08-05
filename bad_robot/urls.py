from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
import datetime

from bad_robot import views

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}
route = routers.DefaultRouter()

# # 注册新的路由地址
# route.register('student', views.StudentViewSet)
# route.register('activity', views.ActivityViewSet)
# route.register('user', views.UserViewSet)
# route.register('join_activity', views.ActivityJoinViewSet)


# 注册上一级的路由地址并添加
urlpatterns = [
    path('search_activity/', views.search_activity),
    path('join_activity/', views.join_activity),
    path('cancel_activity/', views.cancel_activity),
    # path('badminton/login/', obtain_jwt_token),
]