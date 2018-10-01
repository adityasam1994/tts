from django.urls import path, include
from . import views
from .views import play, talk, back, train

app_name = 'page'

urlpatterns = [
    path('play', views.play, name='play'),
    path('talk', views.talk, name='talk'),
    path('back', views.back, name='back'),
    path('train', views.train, name='train'),
    ]
