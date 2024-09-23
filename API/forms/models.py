from django.db import models


class Form(models.Model):
    user = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    question1 = models.TimeField()
    question2 = models.IntegerField()
    question3 = models.TimeField()
    question4 = models.IntegerField()
    question5a = models.IntegerField()
    question5b = models.IntegerField()
    question5c = models.IntegerField()
    question5d = models.IntegerField()
    question5e = models.IntegerField()
    question5f = models.IntegerField()
    question5g = models.IntegerField()
    question5h = models.IntegerField()
    question5i = models.IntegerField()
    question5j = models.IntegerField(null=True, blank=True)
    question5jTitle = models.CharField(max_length=255, null=True, blank=True)
    question6 = models.IntegerField()
    question7 = models.IntegerField()
    question8 = models.IntegerField()
    question9 = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.date.strftime('%Y-%m-%d')}"
