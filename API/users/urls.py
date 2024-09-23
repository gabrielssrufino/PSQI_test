from django.urls import path
from . import views


urlpatterns = [
    path('verify-email/', views.VerifyCreateUser.as_view(), name='verify_or_create_user'),
]
