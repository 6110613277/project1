from django.contrib import admin
from .models import Course, Student
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ("idsubject", "subject", "term", "year", "seat", "status")


admin.site.register(Course, CourseAdmin)
admin.site.register(Student)