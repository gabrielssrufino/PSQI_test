from django.contrib import admin
from .models import Form


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'question1', 'question2', 'question3', 'question4', 'question5a', 'question5b', 'question5c', 'question5d', 'question5e', 'question5f', 'question5g', 'question5h', 'question5i', 'question5j', 'question6', 'question7', 'question8', 'question9']
