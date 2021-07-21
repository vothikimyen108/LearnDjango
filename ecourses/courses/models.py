from django.db import models
from django.contrib.auth.models import AbstractUser
#import lớp chứng thưc


class User(AbstractUser):
    avatar = models.ImageField(upload_to='upload/')
# Create your models here.
#kế thừa, không cần khai báo khóa chính, từ động nó tạo ra, chỉ trừ khi muốn tạo ra
class Category(models.Model):
    name = models.CharField(max_length= 100, null=False, unique=True)#không được null, unique là không đc hai cate trùng nhau

    def __str__(self):
        return self.name

class Course(models.Model):
    subject = models.CharField(max_length= 100, null=False, unique=True)
    description = models.TextField(null=True,blank=False)
    cteate_date = models.DateTimeField(auto_now_add=True)#tự động cập nhật ngày hiện tại lần đầu tiến lúc add
    update_date = models.DateTimeField(auto_now=True)#luôn lấy now thời điểm hiện tại, luôn cập nhật
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)#xử lý khi xóa thể loại thì sao ondelete, thể loại xóa thì cái  null

