from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class userData(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    phone =models.PositiveBigIntegerField()
    img =models.ImageField(upload_to='userimg/',blank=True)
    address=models.CharField(max_length=200)

    def __str__(self):
     return self.user.username


