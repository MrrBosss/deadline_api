from django.db import models
from datetime import datetime
# Create your models here.



class Developer(models.Model):
    developer_image = models.ImageField(upload_to='images', null=True, blank=True)
    developer_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.developer_name)
    
    class Meta:
        verbose_name = 'Dasturchi'
        verbose_name_plural = 'Dasturchilar'


class Process(models.Model):
    status = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Jarayon'
        verbose_name_plural = 'Jarayonlar'


def upload_to(instance, filename):
    # Generate filename here
    if instance.created_at:
        date_str = instance.created_at.strftime("%Y/%m/%d")
    else:
        date_str = datetime.now().strftime("%Y/%m/%d")  # Or use any default date

    return f'{date_str}/{filename}'


class Domain(models.Model):
    field = models.CharField(max_length=50)

    def __str__(self):
        return str(self.field)
    
    class Meta:
        verbose_name = "Yo'nalish"
        verbose_name_plural = "Yo'nalishlar"


class Project(models.Model):
    developer = models.ManyToManyField(Developer)
    project_name = models.CharField(max_length=250)
    project_image = models.ImageField(upload_to=upload_to, null=True, blank=True)
    start_day = models.DateField()
    end_day = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    info = models.CharField(max_length=500)
    process = models.ManyToManyField(Process)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'Proyekt'
        verbose_name_plural = 'Proyektlar'
        
