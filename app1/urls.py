from django.urls import path
from app1.views import *
app_name='app1'
urlpatterns=[
    path('app1_siva/',app1_siva,name='app1_siva'),
]
