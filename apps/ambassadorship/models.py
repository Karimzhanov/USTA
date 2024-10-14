from django.db import models

# Create your models here.
class Ambassadorship(models.Model):
    banner = models.ImageField(
        upload_to='banners/',
        blank=True, null=True, 
        verbose_name="Баннер"
        ) 
    title = models.CharField(
        max_length=255, 
        verbose_name="названия"
        )  
    description = models.TextField(
        verbose_name="Описание"
        ) 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Страница Амбассадорство "
        verbose_name_plural = "Страница Амбассадорство"


class AmbassadorshipImage(models.Model):
    image = models.ImageField(
        upload_to='events/',
        verbose_name="Изображение"
          ) 
    description = models.CharField(
        max_length=255,
        verbose_name="Описания"
        )  

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Ключевое мероприятие"
        verbose_name_plural = "Ключевые мероприятия"