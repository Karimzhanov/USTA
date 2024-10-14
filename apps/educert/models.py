from django.db import models

# Create your models here.
class Educert(models.Model):
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



class Contentblock(models.Model):
    CATEGORY_CHOICES = [
        ('community', 'Преимущества для сообщества'),
        ('events', 'Преимущества для мероприятий'),
        ('suppliers', 'Поставщики'),
        ('partners', 'Партнеры'),
    ]   
    
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        verbose_name="Категория"
        ) 
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
        )  
    image = models.ImageField(
        upload_to='content_images/',
        verbose_name="Изображение", 
        null=True, blank=True
        )  
    description = models.TextField(
        verbose_name="Описание"
        ) 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Контентный блок"
        verbose_name_plural = "Контентные блоки"


class Videoo(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
        )  
    description = models.TextField(
        verbose_name="Описание"
        ) 
    video_url = models.URLField(
        max_length=500, 
        blank=True, null=True,
        verbose_name="Ссылка на видео"
        )  
    image = models.ImageField(
        upload_to='content_images/',
        blank=True, null=True, 
        verbose_name="Изображение"
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео "
