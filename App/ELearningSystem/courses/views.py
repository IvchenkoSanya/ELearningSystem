from .models import Course
from django.shortcuts import render, get_object_or_404

"""from .models import Course"""


def course_list(request):
    courses = Course.objects.filter(is_approved=True)
    return render(request, 'courses/course_list.html', {'courses': courses})


def full_course(request):
    courses = Course.objects.filter(is_approved=True)
    return render(request, 'courses/full_course.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})