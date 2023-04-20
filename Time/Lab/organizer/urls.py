from django.urls import path, include
from .views import main


urlpatterns = [
    path('', main),
    path('register', include('Registration.urls'), name='registration'),
<<<<<<< HEAD
    path('create/', main, name='create'),
=======
>>>>>>> 0736dcc094a51c6d7002eac187b645c382e98b2b
]