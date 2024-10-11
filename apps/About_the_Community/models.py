from django.db import models

# Create your models here.
class About(models.Model):
    banner = models.ImageField(upload_to='banners/', blank=True, null=True, verbose_name="Баннер") 
    title = models.CharField(max_length=255, verbose_name="Заголовок")  
    description = models.TextField(verbose_name="Описание") 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Содержимое страницы"
        verbose_name_plural = "Содержимое страниц"


class CommunityImage(models.Model):
    image = models.ImageField(upload_to='community/', verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание видео")  

    def __str__(self):
        return self.description