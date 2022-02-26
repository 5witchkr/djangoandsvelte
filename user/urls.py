from django.conf.urls import url
from django.urls import path
from .views import Start, Regist, Login

urlpatterns = [
    path('start', Start.as_view(), name='start'),
    path('regist', Regist.as_view(), name='regist'),
    path('login', Login.as_view(), name='login'),
]