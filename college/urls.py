from django.urls import path

from .import views

urlpatterns = [
    # edit
    path('edit/student/<student_id>', views.edit_student_info, name='edit_student_info'),
    path('edit/teacher/<teacher_id>', views.edit_teacher_info, name='edit_teacher_info'),
    # show
    path('show/student/', views.show_students_info, name='show_students_info'),
    path('show/student/education_history', views.show_students_education_history, name='show_students_education_history'),
    path('show/teacher/', views.show_teachers_info, name='show_teachers_info'),
    path('show/student/<studentId>/<studentLastname>', views.show_student_info, name='show_students_info'),
    path('show/student/education_history/<studentId>/<studentLastname>', views.show_student_education_history_info, name='show_student_education_history_info'),
    path('show/teacher/<teachertId>/<teacherLastname>', views.show_teacher_info, name='show_teacher_info'),
    path('show/student/search', views.search_student_list.as_view(), name='search_student_list'),
    path('show/teacher/search', views.search_teacher_list.as_view(), name='search_teacher_list'),
    # register
    path('register/student/', views.register_student, name='register_student'),
    path('register/student/student_term', views.add_student_term, name='add_student_term'),
    path('register/student/payment', views.add_student_payment, name='add_student_payment'),
    path('register/teacher/', views.register_teacher, name='register_teacher'),
    path('register/teacher/teacher_term', views.add_teacher_term, name='add_teacher_term'),
]
