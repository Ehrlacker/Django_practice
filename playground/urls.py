from django.urls import path
from . import views

# URLConf
# Map URLS to view functions
# This is how we handle URL's. If a user goes to /hello, they will be delivered the info contained in the say_hello function in views.hello
urlpatterns = [
    path('hello/', views.say_hello),
    path('goodbye/', views.say_goodbye),
    path('location/', views.location)
]