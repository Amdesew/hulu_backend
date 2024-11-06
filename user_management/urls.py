from django.urls import path
from user_management.views import UserList

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
]
