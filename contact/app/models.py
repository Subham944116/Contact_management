from django.db import models

# Create your models here.

class Contact(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=60)
    cemail=models.CharField(max_length=50,null=True)
    cno=models.IntegerField()

    def __str__(self):
        return self.cname
    
