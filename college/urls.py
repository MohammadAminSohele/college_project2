from django.urls import path

from .import views

urlpatterns = [
    path('show/student/', views.show_students_info, name='show_students_info'),
    path('show/student/detail', views.show_student_info, name='show_students_info'),
    path('show/student/search', views.search_student_list.as_view(), name='search_student_list'),
    path('register/student/', views.register_student, name='register_student'),
    path('register/student/student_term', views.add_student_term, name='add_student_term'),
    path('register/teacher/', views.register_teacher, name='register_teacher'),
    path('register/student/teacher_term', views.add_teacher_term, name='add_teacher_term'),
]
