from django.urls import path
from . import views

# URLConf
# Map URLS to view functions
urlpatterns = [
    path('hello/', views.say_hello)
]