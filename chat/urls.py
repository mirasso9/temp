# chatbot/urls.py

from django.urls import path
from .views import chatbot_view

urlpatterns = [
    path('chatbot_view/', chatbot_view, name='chatbot_view'),
]
