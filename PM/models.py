from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True);
    name = models.CharField(max_length=255);
    email = models.CharField(max_length=25);
    sub = models.CharField(max_length=100);
    msg = models.CharField(max_length=1000);
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True);

    def __str__(self):
        return 'Message from:'  + self.name;
    