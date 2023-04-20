from django.urls import path, include
from .views import main


urlpatterns = [
    path('', main),
    path('register', include('Registration.urls'), name='registration'),

    path('create/', main, name='create'),
]