from rest_framework.serializers import ModelSerializer
from .models import Course, Tag, Lesson

#viết api
# khái báo class khóa học
#Kết thùa lại lớp HyperlinkedModelSerializer
# nó sẻ trả ra json
class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course #chỉ định model
        fields = ['id', 'subject', 'created_date','category_id']  #lấy các trường lấy hết __all__

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag #chỉ định model
        fields = ['id', 'name']


class LessonSerializer(ModelSerializer):
    tags = TagSerializer(many=True) #mối quan hệ manny to manny

    class Meta:
        model = Lesson#chỉ định model
        fields = ['id', 'subject', 'content', 'created_date', 'course', 'tags']


