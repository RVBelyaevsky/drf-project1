from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()

    def get_count_lessons(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = ('course_title', 'course_description', 'count_lessons')


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
