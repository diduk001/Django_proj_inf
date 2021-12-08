import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self) -> str:
        return f'Question: "{self.question_text}", published at {str(self.pub_date)}'

    def published_recently(self) -> bool:
        return timezone.now() - self.pub_date <= datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'Choice: "{self.question}" - "{self.choice_text}" - {self.votes} votes'
