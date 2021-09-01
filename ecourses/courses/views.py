from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets, permissions

# luôn có request từ ui gửi lên
from .models import Course
from .serializers import CourseSerializer


def index(request):
    return render(request,template_name="index.html",context={'name':'kiem yến'});

def welcome(request,year):
    return HttpResponse("hello"+str(year)); #Ep chuoi
#cách 1
def welcome2(request,year_2):
    return HttpResponse("hello 2"+str(year_2)); #Ep chuoi

#cách 2 dùng class hiển thị view
class TestView(View):
    def get(self, request):
        return HttpResponse("get Test")
    def post(self, request):
        pass

#view api xem danh khóa học còn hoạt động
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True) # chỉ định câu truy vấn
    serializer_class = CourseSerializer
    #permission_classes = [permissions.IsAuthenticated] #user đã đăng nhập
    #ghi đè phân quyền
    def get_permissions(self):
        if self.action =="list":
            return [permissions.AllowAny]
        else:
            return [permissions.IsAuthenticated]

    #list -> api danh sách khóa học
    # khóa học chi tiết
    #post khóa học
    # put cập nhật khóa học
