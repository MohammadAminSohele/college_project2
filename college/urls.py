from django.urls import path

from .import views

urlpatterns = [
    path('register/student/', views.register_student, name='register_student'),
    path('register/student/student_term', views.add_student_term, name='add_student_term'),
    path('register/teacher/', views.register_teacher, name='register_teacher'),
    path('register/student/teacher_term', views.add_teacher_term, name='add_teacher_term'),
]
