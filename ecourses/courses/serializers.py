from rest_framework.serializers import ModelSerializer
from .models import Course, Tag, Lesson, User, Category, Comment

#viết api
# khái báo class khóa học
#Kết thùa lại lớp HyperlinkedModelSerializer
# nó sẻ trả ra json
class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course #chỉ định model
        fields = ['id', 'subject', 'created_date','category_id','image']  #lấy các trường lấy hết __all__

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag #chỉ định model
        fields = ['id', 'name']


class LessonSerializer(ModelSerializer):
    tags = TagSerializer(many=True) #mối quan hệ manny to manny

    class Meta:
        model = Lesson#chỉ định model
        fields = ['id', 'subject', 'content', 'created_date', 'course', 'tags']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email', 'username', 'password', 'avatar']
        extra_kwargs = {
            'password':{'write_only':'true'} #chỉ để ghi thui k get ra nè kkk
        }

    def create(self, validated_data):
        user = User(**validated_data) # tự động truyền tham số
        user.set_password(validated_data['password'])
        user.save()

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Lesson#chỉ định model
        fields = ['__all__']