from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic.base import TemplateView


urlpatterns = [
    path('ConnectionTest/', views.httpres),
    url(r'^post/festget/$', views.Festivalget),
    url(r'^run/$', views.run),
    path('post/', views.post_list, name='post_list'),
]