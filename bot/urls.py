from django.urls import path
from . import views


urlpatterns = [
    path('initialize data/', views.initialize_data, name='initialize_data'),
    path('save_word/<str:word>/', views.save_word, name='save_word'),
    path('initialize/', views.initialize, name='initialize'),
    path('install/', views.madeline_view, name='madeline_install')

]
