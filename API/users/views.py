from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserEmailSerializer


class VerifyCreateUser(APIView):

    def post(self, request):
        email = request.data.get('email')

        if not email:
            return Response({'error': 'Email is required', 'status_code': status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_email = User.objects.get(email=email)
            serializer = UserEmailSerializer(user_email)
            return Response({'data': serializer.data, 'status_code': status.HTTP_200_OK}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            serializer = UserEmailSerializer(data={'email': email})
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data, 'status_code': status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
            return Response({'error': serializer.errors, 'status_code': status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
