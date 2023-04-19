from django.urls import path, include
from organizer import views


urlpatterns = [
    path('', views.main),
    path('register', include('Registration.urls'), name='registration'),
    path('create/', views.main, name='create'),
]