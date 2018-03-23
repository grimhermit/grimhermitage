from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    """Тема, которую создает пользователь"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """возвращает строковое представление модели."""
        return self.text


class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    # С версии 1.9 Джанго в качестве обязательного позиционного
    # аргумента требует указать значение on_delete - надо изучить документацию

    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)

    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Возврщает строковое представление модели."""
        # task 18-2 - done

        text_form = self.text[:50]
        if len(text_form) >= 50:
            text_form = self.text[:50] + "..."

        return text_form
