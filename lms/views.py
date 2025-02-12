from rest_framework import viewsets, status
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, get_object_or_404)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from lms.models import Course, Lesson, CourseSubscription
from lms.paginators import MyPaginator
from lms.permissions import IsOwner
from lms.serializers import CourseSerializer, LessonSerializer, CourseSubscriptionSerializer
from users.permissions import IsModer

from lms.tasks import mailing_course_update_sub


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = MyPaginator

    def get_permissions(self):
        if self.action in ["create"]:
            self.permission_classes = (~IsModer,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action in ["destroy"]:
            self.permission_classes = (IsOwner | ~IsModer,)
        return super().get_permissions()


    # def perform_update(self, serializer):
    #     updated_course = serializer.save()
    #     #mailing_course_update_sub.delay(updated_course)
    #     updated_course.save()
    def partial_update(self, request, pk=None):
        course = get_object_or_404(Course, pk=pk)
        serializer = self.get_serializer(course, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            mailing_course_update_sub.delay(pk)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LessonCreateApiView(CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_class = (~IsModer, IsAuthenticated)


class LessonListApiView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = MyPaginator


class LessonRetrieveApiView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsModer | IsOwner)


class LessonUpdateApiView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsModer | IsOwner)


class LessonDestroyApiView(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    '''permission_classes = (IsAuthenticated, IsOwner, ~IsModer)'''
    permission_class = IsAuthenticated


class CourseSubscriptionListApiView(ListAPIView):
    serializer_class = CourseSubscriptionSerializer
    queryset = CourseSubscription.objects.all()


class CourseSubscriptionApiView(APIView):
    queryset = CourseSubscription.objects.all()
    serializer_class = CourseSubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = CourseSubscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = 'вы отписались'
        else:
            CourseSubscription.objects.create(user=user, course=course_item)
            message = 'вы подписались'
        return Response({"message": message})

