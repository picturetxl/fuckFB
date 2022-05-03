from django.db import models

# Create your models here.


class SingleQuestion(models.Model):

    qid =  models.BigIntegerField('qid', primary_key = True)
    question = models.CharField('question',max_length=300)
    optionA = models.CharField('A',max_length=100)
    optionB = models.CharField('B',max_length=100)
    optionC = models.CharField('C',max_length=100)
    optionD = models.CharField('D',max_length=100)
    answer = models.CharField('answer',max_length=5)
    explain = models.CharField('explain',max_length=500)
    

    def __str__(self):
        return self.qid + '--' + self.question






    
