from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from lms.models import CourseSubscription


@shared_task
def add():
    '''проверочный таск для тестирования'''
    print("hello")


@shared_task
def mailing_course_update_sub(course_id):
    '''Отправка письма подписчику об обновлении курса'''
    sub_course = CourseSubscription.objects.filter(course=course_id)
    print(f"всего подписок = {len(sub_course)} на курс {course_id}")
    for sub in sub_course:
        print(f'отправлено {sub.user.email}')
        send_mail(
            'Обновление курса',
            f'Курс {sub.course.course_title} был изменен',
            from_email=EMAIL_HOST_USER,
            recipient_list=[sub.user.email],
            fail_silently=False,
        )
