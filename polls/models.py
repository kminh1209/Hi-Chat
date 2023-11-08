from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
    
    
#     def __str__(self) -> str:
#         return self.choice_text