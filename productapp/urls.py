from django.urls import include, re_path
from .import views
app_name = 'productapp'
urlpatterns =[
    re_path(r'^search$', views.search, name='search'),
    ]