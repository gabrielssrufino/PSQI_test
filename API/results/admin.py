from django.contrib import admin
from .models import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['user1', 'date', 'quality_score', 'latency_score', 'duration_score', 'efficiency_score', 'disturbances_score', 'medication_score', 'daytime_discomfort_score', 'total_score']
