from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
#import lớp chứng thưc



class User(AbstractUser):
    avatar = models.ImageField(upload_to='upload/')
# Create your models here.
#kế thừa, không cần khai báo khóa chính, từ động nó tạo ra, chỉ trừ khi muốn tạo ra
class Category(models.Model):
    name = models.CharField(max_length= 100, null=False, unique=True)#không được null, unique là không đc hai cate trùng nhau

    def __str__(self):
        return self.name

class ItemBase(models.Model):
    class Meta:
        abstract = True #Khai báo ra một model trừu tượng, khi nó chạy nó k tạo ra lớp này nữa, tạo các lớp con thôi
    subject = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='courses/%Y/%m', default=None)
    created_date= models.DateTimeField(auto_now_add=True)  # tự động cập nhật ngày hiện tại lần đầu tiến lúc add
    update_date = models.DateTimeField(auto_now=True)  # luôn lấy now thời điểm hiện tại, luôn cập nhật
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject

#khóa học kế thùa ItemBase
class Course(ItemBase):
    class Meta:
        unique_together = ('subject','category') #Trong một danh mục không được trùng tên khóa học
        ordering = ["-id"] # sắp xếp khi truy vấn id tăng giảm -id, sắp xếp theo nhiều trường mình quy định, có thể ghi đè lại

    description = models.TextField(null=True,blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)#SET_NULL khi thể loại xóa thì khóa bị set null chứ k bị xóa theo


class Lesson(ItemBase):
    class Meta:
        unique_together = (
        'subject', 'course')  # Trong cùng một khóa học (Course) không được trùng tên (subject) bài học (Lesson)
        #db_table: "..." # cách đổi tên bảng.

    #content = models.TextField()
    content = RichTextField() #Tích hợp công cụ edit
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    # on_delete=models.CASCADE: Cấm --> Khóa học xóa thì nó bị xóa theo
    #on_delete=models.SET_DEFAULT: Khi Course của Lesson bị xóa đi, các bạn muốn cho Lesson này thuộc vào cái Course mặc định
    #on_delete=models.PROTECT: Cấm --> Khi những Course có những Lesson thì không được xóa những Course đó
    tags = models.ManyToManyField('Tag', related_name="lessons", blank=True, null=True)   #blank=True: được phép rỗng     #Many to many



class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name