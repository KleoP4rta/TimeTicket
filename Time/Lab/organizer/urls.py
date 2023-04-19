from django.urls import path, include
from .views import main


urlpatterns = [
    path('', views.main),
    path('register', include('Registration.urls'), name='registration'),
    path('create/', views.main, name='create'),
]