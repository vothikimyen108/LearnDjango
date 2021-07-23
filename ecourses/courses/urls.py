from django.urls import path, re_path
from . import views
from django.contrib import admin
from .admin import admin_site
urlpatterns = [
    # path('admin/', admin_site.urls),
    path('admin/', admin.site.urls),
    path('test/', views.TestView.as_view()), #class view get
    re_path(r'^welcome2/(?P<year_2>[0-9]{1,2})/$',views.welcome2), #dùng biểu thức chính quy
    path('welcome/<int:year>', views.welcome, name="welcome"),
    path('', views.index, name="index") #lấy view.index
]