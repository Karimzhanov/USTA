from django.db import models

class PageContent(models.Model):
    logo = models.ImageField(upload_to='logos/', blank=True, null=True, verbose_name="Логотип")  
    banner = models.ImageField(upload_to='banners/', blank=True, null=True, verbose_name="Баннер") 
    title = models.CharField(max_length=255, verbose_name="Заголовок")  
    description = models.TextField(verbose_name="Описание") 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Содержимое страницы"
        verbose_name_plural = "Содержимое страниц"


class ContentBlock(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    date = models.DateField(blank=True, null=True, verbose_name="Дата")
    image = models.ImageField(upload_to='content_images/', blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Контентный блок"
        verbose_name_plural = "Контентные блоки"


class Partner(models.Model):
    logo = models.ImageField(upload_to='partner_logos/', verbose_name="Логотип партнёра")
    name = models.CharField(max_length=255, verbose_name="Название партнёра")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Партнёр"
        verbose_name_plural = "Партнёры"


class EventImage(models.Model):
    image = models.ImageField(upload_to='event_images/', verbose_name="Изображение мероприятия")  
    event = models.ForeignKey('Event', related_name='images', on_delete=models.CASCADE, verbose_name="Мероприятие")

    def __str__(self):
        return f"Image for {self.event.title}"

    class Meta:
        verbose_name = "Изображение мероприятия"
        verbose_name_plural = "Изображения мероприятий"


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок мероприятия") 
    description = models.TextField(verbose_name="Описание мероприятия")
    additional_text = models.TextField(blank=True, null=True, verbose_name="Дополнительный текст")  

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


class ProjectImage(models.Model):
    image = models.ImageField(upload_to='project_images/', verbose_name="Изображение проекта")
    project = models.ForeignKey('ProjectParticipation', related_name='images', on_delete=models.CASCADE, verbose_name="Проект")

    def __str__(self):
        return f"Image for {self.project.title}"

    class Meta:
        verbose_name = "Изображение проекта"
        verbose_name_plural = "Изображения проектов"


class ProjectParticipation(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок проекта") 
    description = models.TextField(verbose_name="Описание проекта") 
    additional_text = models.TextField(blank=True, null=True, verbose_name="Дополнительный текст")  

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Участие в проекте"
        verbose_name_plural = "Участия в проектах"
    

class TeamMember(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")  
    position = models.CharField(max_length=255, verbose_name="Должность")  
    photo = models.ImageField(upload_to='team_photos/', verbose_name="Фото") 

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Член команды"
        verbose_name_plural = "Члены команды"


class Ambassador(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название посла")
    image = models.ImageField(upload_to='ambasador/', verbose_name="Изображение посла")  
    description = models.TextField(verbose_name="Описание посла") 
    additional_text = models.TextField(blank=True, null=True, verbose_name="Дополнительный текст")  

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Посол"
        verbose_name_plural = "Послы"


class Education(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название образования")
    image = models.ImageField(upload_to='education/', verbose_name="Изображение образования")  
    description = models.TextField(verbose_name="Описание образования") 
    additional_text = models.TextField(blank=True, null=True, verbose_name="Дополнительный текст")  

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образования"
    
class Сommunities(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название сообщества")
    image = models.ImageField(upload_to='communities/', verbose_name="Изображение сообщества")  
    description = models.TextField(verbose_name="Описание сообщества") 
    additional_text = models.TextField(blank=True, null=True, verbose_name="Дополнительный текст")  

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сообщество"
        verbose_name_plural = "Сообщества"


class Membership(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название членства")
    image = models.ImageField(upload_to='membership/', verbose_name="Изображение членства")  
    description = models.TextField(verbose_name="Описание членства") 
    additional_text = models.TextField(blank=True, null=True, verbose_name="Дополнительный текст")  

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Членство"
        verbose_name_plural = "Членства"


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название услуги")
    image = models.ImageField(upload_to='service/', verbose_name="Изображение услуги")  
    description = models.TextField(verbose_name="Описание услуги") 
    additional_text = models.TextField(blank=True, null=True, verbose_name="Дополнительный текст")  

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
