
from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.SignUp.as_view(), name="signup")
]
