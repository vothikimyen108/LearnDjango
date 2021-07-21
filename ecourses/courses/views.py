from django.http import HttpResponse
from django.shortcuts import render


# luôn co request từ ui gửi lên
def index(request):
    return render(request,template_name="index.html",context={'name':'kiem yến'});