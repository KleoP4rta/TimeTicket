from django.urls import path, include
from organizer import views


urlpatterns = [
    path('', main),
    path('register', include('Registration.urls'), name='registration'),
    path('create/', main.views, name='create'),
]