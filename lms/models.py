from django.db import models

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    course_title = models.CharField(max_length=255, verbose_name="Название курса")
    course_description = models.TextField(verbose_name="Описание курса", **NULLABLE)
    preview = models.ImageField(upload_to="lms/course_img", verbose_name="превью", **NULLABLE)

    def __str__(self):
        return self.course_title

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Lesson(models.Model):
    lesson_title = models.CharField(max_length=255, verbose_name="Название урока")
    lesson_description = models.TextField(verbose_name="Описание урока", **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="курс")
    lesson_video = models.FileField(
        upload_to="lms/lesson_video", verbose_name="видео урока", **NULLABLE
    )
    preview = models.ImageField(upload_to="lms/lesson_img", verbose_name="превью", **NULLABLE)

    def __str__(self):
        return self.lesson_title

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
