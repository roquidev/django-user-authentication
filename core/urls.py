# External modules
from django.urls import path
# Local modules
from .views import home, profile

urlpatterns = [
    path('', home, name='home'),
    path('accounts/profile/', profile, name='profile'),
]
