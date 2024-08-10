from django.urls import path
from . import views

urlpatterns = [
    path('check_ip/', views.check_ip, name='check_ip'),
    path('send-message/', views.send_telegram_message_view, name='send_message'),
    path('webhook/', views.webhook, name='webhook'),
]
