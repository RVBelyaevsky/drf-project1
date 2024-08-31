from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="email", help_text="укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="номер телефона",
        help_text="укажите телефон",
        **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="загрузите аватар", **NULLABLE
    )
    city = models.CharField(max_length=50, verbose_name="город")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"


class Payment(models.Model):
    PAY_CHOICES = (('cash', 'наличные'), ('visa', 'картой'))

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="курс")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="урок")

    amount = models.IntegerField(verbose_name="сумма оплаты")
    created_at = models.DateTimeField(verbose_name="дата создания")
    pay_method = models.CharField(max_length=20, choices=PAY_CHOICES, verbose_name="способ оплаты")

    def __str__(self):
        return f"Оплата для {self.user} на сумму {self.amount}"

    class Meta:
        verbose_name = "оплата"
        verbose_name_plural = "оплаты"
