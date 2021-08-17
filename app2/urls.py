from django.urls import path
from app2.views import *
app_name='app2'
urlpatterns=[
    path('app2_raj/',app2_raj,name='app2_raj'),
]
