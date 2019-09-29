from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): #models.Model означает, что объект Post является моделью Django, так Django поймет, что он должен сохранить его в базу данных.

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # ссылка на другую модель
    title = models.CharField(max_length=200) #так мы определяем текстовое поле с ограничением на количество символов.
    text = models.TextField() #так определяется поле для неограниченно длинного текста.
    created_date = models.DateTimeField(default=timezone.now) #дата и время.
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title