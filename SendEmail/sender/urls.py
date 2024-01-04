from django.contrib import admin
from django.urls import path, include

from .views import SendEmailView

urlpatterns = [
    path('', SendEmailView.as_view()),
]
