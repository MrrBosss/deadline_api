from django.db import models

# Create your models here.



class Process(models.Model):
    status = models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return self.status



class Project(models.Model):
    developer_image = models.ImageField(upload_to='images', null=True, blank=True)
    developer_name = models.CharField(max_length=50)
    project_name = models.CharField(max_length=250)
    project_image = models.ImageField(upload_to='images', null=True, blank=True)
    start_day = models.DateField()
    end_day = models.DateField()
    info = models.CharField(max_length=500)
    process = models.ForeignKey(Process, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.project_name



class Domain(models.Model):
    filed = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)






    