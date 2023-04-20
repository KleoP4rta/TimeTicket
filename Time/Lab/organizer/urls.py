from django.urls import path, include
from .views import *


urlpatterns = [
    path('', main),
    path('register', include('Registration.urls'), name='registration'),

]