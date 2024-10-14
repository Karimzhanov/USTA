from django.db import models

# Create your models here.
class Service(models.Model):
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
        verbose_name = "Услуга  страницы"
        verbose_name_plural = "Услуга страниц"


class ServiceImage(models.Model):
    image = models.ImageField(
        upload_to='services/', 
        verbose_name="Изображение"
        )
    title = models.CharField(
        max_length=255,
        verbose_name="Названия"
        )
    description = models.TextField(
        verbose_name="Описания"
        )

    def __str__(self):
        return self.title
    
    class Meta: 
        verbose_name = "услуг"
        verbose_name_plural = "услуги"  

    


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок") 
    image = models.ImageField(upload_to='article_images/', blank=True, null=True, verbose_name="Изображение")  
    description = models.CharField(max_length=500, verbose_name="Краткое описание")  

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Services(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок "
        ) 
    description = models.TextField(
        verbose_name="Описание"
        ) 
    additional_text = models.TextField(
        blank=True, null=True, 
        verbose_name="Дополнительный текст"
        )  

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Участие в проекте"
        verbose_name_plural = "Участия в проектах"