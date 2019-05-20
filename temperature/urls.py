from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'$^', views.home),
    url('temperature/post/', views.post_temperature, name='test_post') 
]