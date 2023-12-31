from django.urls import path

from .import views

urlpatterns = [
    # edit
    path('edit/student/<student_id>', views.edit_student_info, name='edit_student_info'),
    path('edit/teacher/<teacher_id>', views.edit_teacher_info, name='edit_teacher_info'),
    # show
    path('show/student/', views.show_students_info.as_view(), name='show_students_info'),
    path('show/student/payment_history', views.students_payment_history, name='students_payment_history'),
    path('show/teacher/payment_history', views.show_teachers_history, name='show_teachers_history'),
    path('show/student/education_history', views.show_students_education_history, name='show_students_education_history'),
    path('show/teacher/', views.show_teachers_info, name='show_teachers_info'),
    # path('show/student/<studentId>/<studentLastname>', views.show_student_info, name='show_students_info'),
    path('show/student/<studnt_term>/', views.show_student_by_studnt_term, name='show_student_by_studnt_term'),
    path('show/teacher/<term>/', views.show_teacher_by_term, name='show_teacher_by_term'),
    path('show/student/payment/<studnt_term>/', views.show_student_payment_by_studnt_term, name='show_student_payment_by_studnt_term'),
    path('show/student/payment_history/<studentId>/<studentLastname>', views.show_student_payment_history, name='show_student_payment_history'),
    path('show/teacher/payment_history/<teacherId>/<teacherLastname>', views.show_teacher_payment_history, name='show_teacher_payment_history'),
    path('show/student/education_history/<studentId>/<studentLastname>', views.show_student_education_history_info, name='show_student_education_history_info'),
    path('show/teacher/<teachertId>/<teacherLastname>', views.show_teacher_info, name='show_teacher_info'),
    path('show/student/search', views.search_student_list.as_view(), name='search_student_list'),
    path('show/teacher/search', views.search_teacher_list.as_view(), name='search_teacher_list'),
    # register
    path('register/student/', views.register_student, name='register_student'),
    path('register/student/student_term', views.add_student_term, name='add_student_term'),
    path('register/student/payment', views.add_student_payment, name='add_student_payment'),
    path('register/teacher/payment', views.add_teacher_payment, name='add_teacher_payment'),
    path('register/teacher/', views.register_teacher, name='register_teacher'),
    path('register/teacher/teacher_term', views.add_teacher_term, name='add_teacher_term'),
]
