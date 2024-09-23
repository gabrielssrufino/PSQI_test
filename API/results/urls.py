from django.urls import path
from . import views


urlpatterns = [
    path('results/list/', views.ResultHistory.as_view(), name='result_history'),
]
