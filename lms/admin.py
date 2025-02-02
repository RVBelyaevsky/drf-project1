from django.contrib import admin

from lms.models import Course, Lesson, CourseSubscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'course_title')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'lesson_title')


@admin.register(CourseSubscription)
class CourseSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'course')

