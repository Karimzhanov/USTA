from django.db import models

# Create your models here.
class Events(models.Model):
    banner = models.ImageField(
        upload_to='banners/',
        blank=True, null=True, 
        verbose_name="Баннер"
        ) 
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
        )  
    description = models.TextField(
        verbose_name="Описание"
        ) 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие страницы"
        verbose_name_plural = "Мероприятия страниц"


class Eventss(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название'
        )
    image = models.ImageField(
        upload_to='events/',
        verbose_name='Изображение'
        )
    date = models.DateField(
        verbose_name='Дата'
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"


class Announcement(models.Model):
    title = models.CharField(
        max_length=200, 
        verbose_name='Название'
        )
    description = models.TextField(
        verbose_name='Описание'
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class AnnualEvent(models.Model):
    image = models.ImageField(
        upload_to='events/',
        verbose_name="Изображение"
          ) 
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
        )  

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ключевое мероприятие"
        verbose_name_plural = "Ключевые мероприятия"


class VideoContent(models.Model):
    thumbnail = models.ImageField(
        upload_to='video_thumbnails/',
        verbose_name="Миниатюра видео"
        ) 
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок видео"
        )  
    description = models.TextField(
        verbose_name="Описание видео"
        )  
    video_url = models.URLField(
        verbose_name="URL видео"
        )  

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видеоматериалы"


class VideoContents(models.Model):
    thumbnail = models.ImageField(
        upload_to='video_thumbnails/',
        verbose_name="Миниатюра видео"
        ) 
    title = models.CharField(
        max_length=255, 
        verbose_name="Заголовок видео"
        )  
    description = models.TextField(
        verbose_name="Описание видео"
        )  
    video_url = models.URLField(
        verbose_name="URL видео"
        )  

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видеоматериалы"
