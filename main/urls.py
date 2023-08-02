
from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UsersAPI.as_view()),
    path('counter/', CounterAPIView.as_view()),
    path('counter/delete_all/', CounterAPIView.as_view()),
]
