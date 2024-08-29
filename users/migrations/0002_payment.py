# Generated by Django 4.2.2 on 2024-08-29 02:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0002_alter_course_preview_alter_lesson_lesson_video_and_more"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.IntegerField(verbose_name="сумма оплаты")),
                ("created_at", models.DateTimeField(verbose_name="дата создания")),
                (
                    "pay_method",
                    models.CharField(
                        choices=[("cash", "наличные"), ("visa", "картой")],
                        max_length=20,
                        verbose_name="способ оплаты",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lms.course",
                        verbose_name="курс",
                    ),
                ),
                (
                    "lesson",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lms.lesson",
                        verbose_name="урок",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "оплата",
                "verbose_name_plural": "оплаты",
            },
        ),
    ]
