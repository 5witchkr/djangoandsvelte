from django.conf.urls import url
from django.urls import path
from .views import Main, Create, Detail

urlpatterns = {
    path('main', Main.as_view(), name='main'),
    path('create', Create.as_view(), name='create'),
    path('detail', Detail.as_view(), name='detail'),
}