from django.urls import path
from . import views


urlpatterns = [
    path('forms/send/', views.CreateFormView.as_view(), name='send_form'),
    path('forms/list/', views.ListFormView.as_view(), name='send_form'),
]
