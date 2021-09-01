from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Course
#viết api
# khái báo class khóa học
#Kết thùa lại lớp HyperlinkedModelSerializer
# nó sẻ trả ra json
class CourseSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Course #chỉ định model
        fields = ['id', 'subject', 'created_date','category_id']  #lấy các trường lấy hết __all__
