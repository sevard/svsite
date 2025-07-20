from django.urls import path
from . import views


app_name = 'webtools'
urlpatterns = [
    # ex: /webtools/sha_func/
    path('sha/', views.sha_functions, name='sha-functions'),
    # ex: /webtools/iplookup/
    path('iplookup/', views.ip_lookup, name='iplookup'),
]