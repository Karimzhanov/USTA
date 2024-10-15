from django.db import models

# Create your models here.
class Membership(models.Model):
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
        verbose_name = "Содержимое Членоствао"
        verbose_name_plural = "Содержимое Членоство"

class ContentBlock(models.Model):
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


class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название категории"
        )
    image = models.ImageField(
        upload_to='categories/',
        verbose_name="Изображение категории")    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class StepInstruction(models.Model):
    step_number = models.PositiveIntegerField(
        verbose_name="Номер шага"
        )  
    title = models.CharField(
        max_length=255, 
        verbose_name="Заголовок шага"
        )  
    description = models.TextField(
        verbose_name="Описание шага"
        )  

    
    def __str__(self):
        return f"Шаг {self.step_number}: {self.title}"

    class Meta:
        verbose_name = "Пошаговая инструкция"
        verbose_name_plural = "Пошаговые инструкции"

