from django.db import models
from django.contrib.auth.models import User

class Muallif(models.Model):
    ism = models.CharField(max_length=100)
    yosh = models.PositiveSmallIntegerField()
    kasb = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=100)
    matn = models.TextField()
    rasm = models.URLField()
    sana = models.DateTimeField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavha
    
class Talks(models.Model):
    sarlavha = models.CharField(max_length=100)
    video = models.URLField()
    sana = models.DateTimeField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavha