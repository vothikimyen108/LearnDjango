from django.urls import path, re_path,include
from . import views
from django.contrib import admin
from rest_framework import routers
from .admin import admin_site
from django.conf.urls.static import static
from django.conf import settings

#khai báo route
router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)# 2 phần phần đầu, và cái view
router.register('lesson', views.LessonViewSet)
router.register('registeruser', views.UserViewSet)
# router.register('category', views.CategoryViewSet)

admin.autodiscover()
urlpatterns = [
     # path('/', admin_site.urls),
    path('admin/', admin.site.urls),
     #path('test/', views.TestView.as_view()), #class view get
      # re_path(r'^welcome2/(?P<year_2>[0-9]{1,2})/$',views.welcome2), #dùng biểu thức chính quy
      # path('welcome/<int:year>', views.welcome, name="welcome"),
      # path('', views.index, name="index") #lấy view.index
    path('', include(router.urls))
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

