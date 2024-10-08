# Generated by Django 4.2.2 on 2024-08-21 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                (
                    "course_title",
                    models.CharField(max_length=255, verbose_name="Название курса"),
                ),
                (
                    "course_description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание курса"
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        upload_to="lms/course_img", verbose_name="превью"
                    ),
                ),
            ],
            options={
                "verbose_name": "курс",
                "verbose_name_plural": "курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
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
                (
                    "lesson_title",
                    models.CharField(max_length=255, verbose_name="Название урока"),
                ),
                (
                    "lesson_description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание урока"
                    ),
                ),
                (
                    "lesson_video",
                    models.FileField(
                        upload_to="lms/lesson_video", verbose_name="видео урока"
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        upload_to="lms/lesson_img", verbose_name="превью"
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
            ],
            options={
                "verbose_name": "урок",
                "verbose_name_plural": "уроки",
            },
        ),
    ]
