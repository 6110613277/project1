from django.urls import path
from . import views
from subjects import views as cv
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:course_idsubject>', views.course, name="course"),
    path('index', cv.index, name='index'),
    path('student', views.student, name="student" ),
    path('add', views.add, name="add"),
]