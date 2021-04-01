from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Mail(models.Model):
    sno=models.AutoField(primary_key=True)
    subject=models.CharField(max_length=50)
    text=models.TextField(default="")
    to=models.CharField(max_length=50)
    sender=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    isStarred=models.BooleanField(default=False)
    timeStamp = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return str(self.to)+' - '+str(self.subject)