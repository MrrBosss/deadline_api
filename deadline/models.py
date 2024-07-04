from django.db import models

# Create your models here.



class Project(models.Model):
    developer = models.CharField(max_length=50)
    developer_i = models.ImageField(upload_to='projects', null=True, blank=True)
    project_name = models.CharField(max_length=250)
    process = models.CharField(max_length=250)
    start_d = models.IntegerField()
    end_d = models.IntegerField()
    info = models.CharField(max_length=500)


class AdditionalInfo(models.Model):
    definition = models.TextField(blank=True,null=True)








    