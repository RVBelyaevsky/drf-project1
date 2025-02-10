from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course, Lesson, CourseSubscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@gmail.com')
        self.course = Course.objects.create(course_title='driver', course_description='course for driving')
        self.lesson = Lesson.objects.create(lesson_title='cars', course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("lms:retrieve", args=(self.lesson.pk,))
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("lesson_title"), self.lesson.lesson_title)

    def test_lesson_create(self):
        url = reverse("lms:create")
        self.client.force_authenticate(user=self.user)
        data = {
            'lesson_title': "motors",
            'course': self.course.pk,
            'lesson_description': 'description'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse('lms:update', args=(self.lesson.pk,))
        data = {
            'lesson_title': 'motors',
            'lesson_description': 'fix motors',
            'course': self.course.pk,
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('lesson_title'), 'motors')

    def test_lesson_delete(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('lms:delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse('lms:list')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@gmail.com')
        self.course = Course.objects.create(course_title='test_course', course_description='descr for test_course')
        self.lesson = Lesson.objects.create(lesson_title='test_lesson', course=self.course, owner=self.user)
        self.subscribe = CourseSubscription.objects.create(user=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_subscribe_to_course(self):
        CourseSubscription.objects.all().delete()
        url = reverse('lms:create_course_sub')
        data = {'course': self.course.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'вы подписались')
