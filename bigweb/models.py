from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #Each model has a number of class variables, each of which represents a database field in the model.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)