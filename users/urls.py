from django.urls import path
from .views import index, profile, RegisterView

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
]