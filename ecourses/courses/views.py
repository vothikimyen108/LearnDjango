from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist
# luôn có request từ ui gửi lên
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from rest_framework.response import Response

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

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active=True)  # chỉ định câu truy vấn
    serializer_class = LessonSerializer

    # viết thêm api cập nhận ẩn bài học
    @action(methods=['post'], detail=True, url_path="hide-lesson", url_name='hide-lesson')
    # /lesson/{pk}/hide-lesson
    def hide_lesson(self, requset, pk):
        try:
            l = Lesson.objects.get(pk=pk)
            l.action = False
            l.save()
        except Lesson.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST) #khi pk không có trong hệ thống
        return Response(data=LessonSerializer(l).data, status=status.HTTP_200_OK)



