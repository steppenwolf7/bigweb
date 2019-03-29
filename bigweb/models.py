from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #Each model has a number of class variables, each of which represents a database field in the model.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

    #Run python manage.py makemigrations to create migrations for those changes
    #Run python manage.py migrate to apply those changes to the database.
    