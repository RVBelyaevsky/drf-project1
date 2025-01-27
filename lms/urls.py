from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.views import (CourseViewSet, LessonCreateApiView,
                       LessonDestroyApiView, LessonListApiView,
                       LessonRetrieveApiView, LessonUpdateApiView)

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="courses")

urlpatterns = [
    path("lessons/create", LessonCreateApiView.as_view(), name="create"),
    path("lessons/", LessonListApiView.as_view(), name="list"),
    path("lessons/<int:pk>/", LessonRetrieveApiView.as_view(), name="retrieve"),
    path("lessons/<int:pk>/update/", LessonUpdateApiView.as_view(), name="update"),
    path("lessons/<int:pk>/delete/", LessonDestroyApiView.as_view(), name="delete"),  # noqa: E501
] + router.urls
