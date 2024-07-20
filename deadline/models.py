from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

# Create your models here.
User = get_user_model()


def upload_to(instance, filename):
    # Generate filename here
    if instance.created_at:
        date_str = instance.created_at.strftime("%Y/%m/%d")
    else:
        date_str = datetime.now().strftime("%Y/%m/%d")  # Or use any default date

    return f'{date_str}/{filename}'


class Task(models.Model):
    name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name
    

class Project(models.Model):  
    name = models.CharField(max_length=250,null=True)
    image = models.ImageField(upload_to=upload_to, null=True)
    start_day = models.DateField()
    end_day = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    direction = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    job = models.ManyToManyField(Job)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Proyekt'
        verbose_name_plural = 'Proyektlar'
        


    