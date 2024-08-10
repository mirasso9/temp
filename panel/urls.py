from django.urls import path
from .views import login_view
from .views import index

urlpatterns = [
    path('login/', login_view, name='login'),
    path('index/', index, name='index'),

]