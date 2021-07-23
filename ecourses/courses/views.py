from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# luôn co request từ ui gửi lên
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