from django.contrib import admin
from django.urls import path
from app.views import home, root

urlpatterns = [
    path('', root),
    path('<name>/', home),
]
