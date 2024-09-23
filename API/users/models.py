from django.db import models


class User(models.Model):
    email = models.CharField(max_length=155, unique=True, primary_key=True)

    def __str__(self):
        return self.email
