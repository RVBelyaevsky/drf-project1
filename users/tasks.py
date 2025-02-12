from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def check_last_login():
    """отключение пользователя не регистрировавшегося месяц"""
    users = User.objects.filter(last_login__isnull=False)
    for user in users:
        if timezone.now() - user.last_login > timedelta(days=31):
            user.is_active = False
            user.save()
            print(f'Пользователь {user.email} отключен')
        else:
            print(f'Пользователь {user.email} активен')
