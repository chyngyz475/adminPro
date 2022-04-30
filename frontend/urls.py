from django.urls import include, path

from frontend.models import frontend

urlpatterns = [
    path('frontend/', frontend, name='frontend')
]
