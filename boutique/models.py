from django.db import models

# Create your models here.
class Article(models.Model):
    prod=models.CharField(max_length=30)
    prix= models.FloatField()
    stat=models.CharField(max_length=30)
    dateCmd=models.DateField()

    def __str__(self) -> str:
        return self.prod    


