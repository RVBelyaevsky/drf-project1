from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Course, Lesson, CourseSubscription
from lms.validators import LinkCheckValidator


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LinkCheckValidator(field='lesson_description')]


class CourseSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()
    lessons = LessonSerializer(many=True, source='lesson_set')
    is_subscribed = SerializerMethodField()

    def get_count_lessons(self, obj):
        return obj.lesson_set.count()

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        return CourseSubscription.objects.filter(course=obj, user=user).exists()

    class Meta:
        model = Course
        fields = ('course_title', 'course_description', 'count_lessons', 'lessons', 'is_subscribed')
        validators = [LinkCheckValidator(field='course_description')]


class CourseSubscriptionSerializer(ModelSerializer):

    class Meta:
        model = CourseSubscription
        fields = "__all__"
