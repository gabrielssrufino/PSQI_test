from rest_framework import serializers
from .models import Result


class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = ['date', 'total_score']
