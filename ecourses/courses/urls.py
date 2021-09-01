from django.urls import path, re_path,include
from . import views
from django.contrib import admin
from rest_framework import routers
from .admin import admin_site


#khai báo route
router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)# 2 phần phần đầu, và cái view



urlpatterns = [
    # path('admin/', admin_site.urls),
    # path('admin/', admin.site.urls),
    path('',include(router.urls)),
    # path('test/', views.TestView.as_view()), #class view get
    # re_path(r'^welcome2/(?P<year_2>[0-9]{1,2})/$',views.welcome2), #dùng biểu thức chính quy
    # path('welcome/<int:year>', views.welcome, name="welcome"),
    # path('', views.index, name="index") #lấy view.index
]