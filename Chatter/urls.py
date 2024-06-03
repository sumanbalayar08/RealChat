from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_home, name='chat_home'),
    path('<str:username>/', views.chat_view, name='chat_view'),
]
