from django.urls import path
from . import views
from subjects import views as cv
from django.conf.urls import url
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('index', cv.index, name='index'),
   path('test', views.test, name='test'),
]