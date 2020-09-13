from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .models import Course
from .models import Student
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

def index(request):
    return render(request, "subjects/test.html", {
        "subjects": Course.objects.all()
    })


def course(request, course_idsubject):
    course = Course.objects.get(idsubject=course_idsubject)
    return render(request, "subjects/course.html", {
        "course": course
    })

def test(request):
    return render(request, "subjects/test.html", {
        "subjects": Course.objects.all()
    })

def student(request, student_first):
    student = Student.objects.get(first=student_first)
    return render(request, "subjects/student.html", {
        "student": student
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password =  request.POST["password"]
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials"
            })
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })

def studentinfo(request,sID):
    print(sID)
    student_info = Student.objects.get(sID=sID)
    class_info = Course.objects.filter(attendStd = student_info)
    non_classinfo = Course.objects.exclude(attendStd = student_info).all()
    logged = logout_view
    context = {'student_info': student_info, "class_info":class_info, "non_classinfo":non_classinfo, "logged1":logged,}

    return context

def add(request):
    if request.method == "POST":
        addsubject = request.POST["Course.object.first()"]
        addsubject.append(addsubject)
        return HttpResponseRedirect(reverse("index"))
    else:
        return HttpResponseRedirect(reverse("index"))