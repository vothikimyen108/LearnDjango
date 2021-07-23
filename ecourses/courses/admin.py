from django.contrib import admin
from django import forms
from django.db.models import Count
from django.template.response import TemplateResponse
from django.urls import path
from .models import Category, Course, Lesson, Tag,User
from django.contrib.auth.models import Permission
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.html import mark_safe #để tránh xẩy ra lỗi import thư viện này


#tạo lớp from tích hợp ghi đè vô
class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'
#custormer để nó hiện sẳn lesson
class LessonInlineAdmin(admin.StackedInline):
    model = Lesson
    fk_name = 'course' # tên khoá ngoại (tuỳ chọn)
#manyto many
class LessonTagInlineAdmin(admin.StackedInline):
    model = Lesson.tags.through

#custom tranng lesson
class LessonAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('/static/css/main.css',)#thêm css thêm đc nhiều đằng sau ,
        }

    form = LessonForm #hiện upload tập tin
    list_display = ["id", "subject", "created_date", "course"]
    search_fields = ["subject", "created_date", "course__subject"]
    list_filter = ["subject", "course__subject"]
    readonly_fields = ["avatar"]
    #làm coustom nó hiện ảnh
    def avatar(self, lesson):
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' width='120px'/>".format(img_url=lesson.image.name, alt=lesson.subject))

    inlines = [LessonTagInlineAdmin, ]

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInlineAdmin, ]
class TagAdmin(admin.ModelAdmin):
    inlines = [LessonTagInlineAdmin, ]

#admind site thiết kế lại ui
class CourseAppAdminSite(admin.AdminSite):
    site_header = 'Hệ thống khoá học trực tuyến'

    def get_urls(self):
        return [
                   path('course-stats/', self.course_stats)
               ] + super().get_urls() #nối 2 dánh sách lại

    def course_stats(self, request):
        course_count = Course.objects.count()
        stats = Course.objects.annotate(lesson_count=Count('lessons')).values("id", "subject",
                                                                              "lesson_count")  # lessons: là related_name của biến course trong models
        return TemplateResponse(request, 'admin/course-stats.html', {
            'course_count': course_count,
            'stats': stats
        })

#tạo đối tượng admin site
admin_site = CourseAppAdminSite('mycouses');

# Register your models here.
#thêm catogory vô trang admin
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
#custom lại adminsite nè
# admin_site.register(Course,CourseAdmin)
