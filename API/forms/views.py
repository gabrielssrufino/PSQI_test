from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Form
from results.models import Result
from .serializers import FormSerializer
from .utils import translate_psqi, calculate_psqi_scores


class CreateFormView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

        translated_data = translate_psqi(data)
        user_email = data.get('user')

        form = Form(
            user=user_email,
            question1=translated_data['question1'],
            question2=translated_data['question2'],
            question3=translated_data['question3'],
            question4=translated_data['question4'],
            question5a=translated_data['question5a'],
            question5b=translated_data['question5b'],
            question5c=translated_data['question5c'],
            question5d=translated_data['question5d'],
            question5e=translated_data['question5e'],
            question5f=translated_data['question5f'],
            question5g=translated_data['question5g'],
            question5h=translated_data['question5h'],
            question5i=translated_data['question5i'],
            question5j=translated_data['question5j'],
            question5jTitle=translated_data['question5jTitle'],
            question6=translated_data['question6'],
            question7=translated_data['question7'],
            question8=translated_data['question8'],
            question9=translated_data['question9']
        )
        form.save()

        scores = calculate_psqi_scores(translated_data)

        Result.objects.create(
            user1=user_email,
            quality_score=scores['quality_score'],
            latency_score=scores['latency_score'],
            duration_score=scores['duration_score'],
            efficiency_score=scores['efficiency_score'],
            disturbances_score=scores['disturbances_score'],
            medication_score=scores['medication_score'],
            daytime_discomfort_score=scores['daytime_discomfort_score'],
            total_score=scores['total_score']
        )

        response_data = {
            'total_score': scores['total_score']
        }

        return Response(response_data, status=status.HTTP_201_CREATED)


class ListFormView(generics.ListAPIView):
    serializer_class = FormSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email', None)
        if email is not None:
            return Form.objects.filter(user=email)
        return Form.objects.all()
