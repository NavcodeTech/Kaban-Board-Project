from django.db import models
from django.db.models import Model
# Create your models here.

class CardInfo(models.Model):
    cardno = models.IntegerField()
    taskname = models.CharField(max_length=20,default='null')
    taskid = models.CharField(max_length=20)
    team = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    expecttime = models.CharField(max_length=20)
    addinfo = models.TextField()
    duedate = models.DateField()


    class Meta:
        db_table = 'CardInfo'

    def __str__(self):
        return self.taskname;
    
class ProgressInfo(models.Model):
    cardno = models.IntegerField()
    taskname = models.CharField(max_length=20,default='null')
    taskid = models.CharField(max_length=20)

    class Meta:
        db_table = 'ProgressInfo'

    def __str__(self):
        return self.taskname
    
class CompleteInfo(models.Model):
    cardno = models.IntegerField()
    taskname = models.CharField(max_length=20,default='null')
    taskid = models.CharField(max_length=20)

    class Meta:
        db_table = 'CompleteInfo'

    def __str__(self):
        return self.taskname;
    

