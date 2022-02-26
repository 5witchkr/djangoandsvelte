from django.conf.urls import url
from django.urls import path
from .views import Testp

urlpatterns = [
    path('testp', Testp.as_view(), name='testp'),
]