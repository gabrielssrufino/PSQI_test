from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Result
from .serializers import ResultSerializer


class ResultHistory(APIView):
    def get(self, request, *args, **kwargs):
        email = request.GET.get('email')

        if not email:
            return Response({'detail': 'Parâmetro "email" é necessário.'}, status=status.HTTP_400_BAD_REQUEST)

        resultados = Result.objects.filter(user1=email).order_by('date')

        serializer = ResultSerializer(resultados, many=True)

        labels = [resultado['date'] for resultado in serializer.data]
        data_points = [resultado['total_score'] for resultado in serializer.data]

        quality_map = []

        for score in data_points:
            if score < 5:
                quality_map.append('Boa qualidade do sono')
            elif score > 5 and score < 10:
                quality_map.append('Pobre qualidade do sono')
            else:
                quality_map.append('Presença de distúrbio do sono')

        chart_data = {
            'labels': labels,
            'data': data_points,
            'quality_map': quality_map
        }

        return Response(chart_data, status=status.HTTP_200_OK)
