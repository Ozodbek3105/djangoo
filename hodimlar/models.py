from django.db import models

# Create your models here.

class Hodim(models.Model):
    ismi = models.CharField(max_length=100)
    familyasi = models.CharField(max_length=100)
    rasmi = models.ImageField(upload_to="rasmlar") 
    mansabi =  models.CharField(max_length=100)
    email =  models.CharField(max_length=50)
    telefon =  models.CharField(max_length=20)
    kirirtilgan_sana = models.DateTimeField(auto_now_add=True)
    yangilagan_sana = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.ismi} {self.familyasi}"
