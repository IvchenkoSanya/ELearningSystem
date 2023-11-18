from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name="courseList"),
    path('full-course', views.full_course, name="course"),
    path('full-course/<int:course_id>/', views.course_detail, name='course_detail'),
]