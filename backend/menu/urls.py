from django.urls import path

from .views import base


urlpatterns = [
    path('home/', base, name='home'),
    path('some/named/url', base, name='named')
]