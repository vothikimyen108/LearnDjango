from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist
# luôn có request từ ui gửi lên
from .models import Course, Lesson, User, Category
from .serializers import CourseSerializer, LessonSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

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
class CourseViewSet(viewsets.ViewSet, generics.ListAPIView,generics.RetrieveAPIView):
    queryset = Course.objects.filter(active=True) # chỉ định câu truy vấn
    serializer_class = CourseSerializer

    # def get_queryset(self):
    #     queryset = Course.objects.all()
    #     categoryid = self.request.query_params.get('category_id', None)
    #     # subject = self.request.query_params.get('q', None)
    #     # if categoryid:
    #     #     queryset = queryset.filter(category_id=categoryid)
    #     # if subject:
    #     #     queryset = queryset.filter(subject=subject)
    #     return queryset

    @action(methods=['get'], detail=True, url_path="lesson", url_name='lesson')
    # /lesson/{pk}/hide-lesson
    def lesson(self, request, pk):
        try:
            c = Course.objects.get(pk=pk)
            queryset = Lesson.objects.filter(course=c)
            q = request.query_params.get("q", None)
            if q:
                queryset = queryset.filter(subject__contains=q)

        except Lesson.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST) #khi pk không có trong hệ thống
        return Response(LessonSerializer(queryset, many=True).data, status=status.HTTP_200_OK)

class LessonViewSet(viewsets.ViewSet, generics.ListAPIView,generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(active=True)  # chỉ định câu truy vấn
    serializer_class = LessonSerializer

    # # viết thêm api lấy bài học
    # @action(methods=['get'], detail=True,)
    # # /lesson/{pk}/hide-lesson
    # def hide_lesson(self, requset, pk):
    #     try:
    #         l = Lesson.objects.get(pk=pk)
    #         l.action = False
    #         l.save()
    #     except Lesson.DoesNotExist:
    #         return Response(status=status.HTTP_400_BAD_REQUEST) #khi pk không có trong hệ thống
    #     return Response(data=LessonSerializer(l).data, status=status.HTTP_200_OK)





#api đăng ký, kết thừa viewset bình thường , generics.CreateAPIView tạo api thêm, lấy thông tin RetrieveAPIView

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)  # chỉ định câu truy vấn
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]
    def get_permissions(self):
        if self.action =="retrieve":
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.AllowAny()]

#view api category

# class CategoryViewSet(viewsets.ViewSet,generics.ListAPIView):
#     queryset = Category
#     serializer_class = CategoriesSerializer
