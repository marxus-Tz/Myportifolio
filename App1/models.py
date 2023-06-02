from django.db import models

# Create your models here.
class projects(models.Model):
    title=models.TextField(max_length=50)
    description=models.TextField(max_length=250)
    image=models.ImageField(upload_to='projects/')
    url=models.URLField(blank=True)
from django.db import models

class ContactMessage(models.Model):
    name=models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email