from django.db import models

# Create your models here.

class Сollaboration(models.Model):
    banner = models.ImageField(
        upload_to='Сollaboration/',
        verbose_name="Фото банера"
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
        verbose_name = "Участие в проекте"
        verbose_name_plural = "Участие в проектах"



class Project(models.Model):
    image = models.ImageField(
        upload_to='projects/',
        verbose_name="Изображение проекта"
        )  
    title = models.CharField(
        max_length=255,
        verbose_name="Название проекта"
        )  
    description = models.CharField(
        max_length=255,
        verbose_name="Описание проекта"
        ) 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

class ProjectsPage(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок страницы"
        ) 
    projects = models.ManyToManyField(
        Project,
        verbose_name="Проекты"
        ) 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Award(models.Model):
    image = models.ImageField(
        upload_to='awards/',
        verbose_name="Изображение награды"
         )  
    title = models.CharField(
        max_length=255,
        verbose_name="Название награды"
        )  
    description = models.TextField(
        verbose_name="Описание награды"
        )  

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Награда"
        verbose_name_plural = "Награды"


class MentoringPrograms(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
        ) 
    image = models.ImageField(
        upload_to='mentoringprograms/',
        verbose_name="Изображение"
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
        verbose_name = "Контентный блок"
        verbose_name_plural = "Контентные блоки"