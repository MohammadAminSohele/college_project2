from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView
from django.http import Http404

from .forms import StudentForm,StudentTermForm,TeacherForm,TeacherTermForm,StudentPaymentForm,TeacherPaymentForm
from .import models

# Create your views here.

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()
    return render(request, 'college/register_student.html', {'form': form,'title':'ثبت اطلاعات دانشجو'})


def register_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TeacherForm()
    return render(request, 'college/register_teacher.html', {'form': form,'title':'ثبت اطلاعات استاد'})


def add_student_term(request):
    if request.method == 'POST':
        form = StudentTermForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page
    else:
        form = StudentTermForm()

    return render(request, 'college/add_student_term.html', {'form': form,'title':'ثبت ترم برای دانشجو'})

def add_student_payment(request):
    if request.method == 'POST':
        form = StudentPaymentForm(request.POST)
        if form.is_valid():
            student=form.cleaned_data.get('student')
            date_of_payment=form.cleaned_data.get('date_of_payment')
            total=form.cleaned_data.get('total')
            price=form.cleaned_data.get('price')
            account=form.cleaned_data.get('account')
            remaining_price=form.cleaned_data.get('remaining_price')
            code=form.cleaned_data.get('code')
            models.Payment.objects.create(student=student,date_of_payment=date_of_payment,total=total,price=price,account=account,remaining_price=remaining_price,code=code)
            form=StudentPaymentForm()
            return redirect('/')  # Redirect to a success page
    else:
        form = StudentPaymentForm()
    return render(request, 'college/add_student_payment.html', {'form': form,'title':'ثبت پرداخت وجه دانشجو'})

def add_teacher_payment(request):
    if request.method == 'POST':
        form = TeacherPaymentForm(request.POST)
        if form.is_valid():
            # form.save()
            teacher=form.cleaned_data.get('teacher')
            date_of_payment=form.cleaned_data.get('date_of_payment')
            hours=form.cleaned_data.get('hours')
            price_in_hour=form.cleaned_data.get('price_in_hour')
            account=form.cleaned_data.get('account')
            total=hours*price_in_hour
            models.TeacherPayment.objects.create(teacher=teacher,date_of_payment=date_of_payment,hours=hours,price_in_hour=price_in_hour,account=account,total=total)
            form=TeacherPaymentForm()
            return redirect('/')  # Redirect to a success page
    else:
        form = TeacherPaymentForm()
    context={
        'title':'ثبت وجه استاد',
        'form':form
    }
    return render(request, 'college/add_teacher_payment.html', context)

def add_teacher_term(request):
    if request.method == 'POST':
        form = TeacherTermForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page
    else:
        form = TeacherTermForm()

    return render(request, 'college/add_teacher_term.html', {'form': form,'title':'ثبت ترم برای استاد'})


def show_students_info(request):
    students=models.Student.objects.all().values('nat_code','first_name','last_name')
    context={
        'students':students,'title':'اطلاعات دانشجویان'
    }
    return render(request,'college/show_students_info.html',context)

def students_payment_history(request):
    students=models.Payment.objects.all()
    for student in students:
        student.remaining_price = student.total - student.price
    context={
        'students':students,'title':'تاریخچه وجه دانشجویان'
        # 'total':students.get_total_price()
    }
    return render(request,'college/students_payment_history.html',context)

def show_teachers_history(request):
    techers_payment=models.TeacherPayment.objects.all()
    context={
        'title':'تاریخچه وجه استادان',
        'techers_payment':techers_payment,
    }
    return render(request,'college/show_teachers_history.html',context)

def show_students_education_history(request):
    students=models.Student.objects.all().values('first_name','last_name','score')
    students_term=models.StudentTerm.objects.all()    
    context={
        'students':students,
        'students_term':students_term,'title':'تاریخچه تحصیلی دانشجویان'
    }
    return render(request,'college/show_students_education_history.html',context)

def show_teachers_info(request):
    teachers=models.Teacher.objects.all().values('nat_code','first_name','last_name')
    context={
        'teachers':teachers,'title':'اطلاعات اساتید'
    }
    return render(request,'college/show_teachers_info.html',context)


class search_student_list(ListView):
    template_name = 'college/search-student-list.html'

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return models.Student.objects.search(query)
        return models.Student.objects.all().values('nat_code','first_name','last_name')

class search_teacher_list(ListView):
    template_name = 'college/search-teacher-list.html'
    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return models.Teacher.objects.search(query)
        return models.Teacher.objects.all().values('nat_code','first_name','last_name')

def show_student_info(request,*args,**kwargs):
    student_id=kwargs['studentId']
    student=models.Student.objects.get_by_id(student_id)
    if student is None:
        raise Http404('دانشجو مورد نظر یافت نشد')
    context={
        'title':'اطلاعات دانشجو',
        'student':student
    }
    return render(request,'college/show_student_info.html',context)


def show_student_by_studnt_term(request,*args,**kwargs):
    studnt_term=kwargs['studnt_term']
    studnt_term=models.StudentTerm.objects.filter(term__name=studnt_term).first()
    if studnt_term is None:
        raise Http404('دانشجویان مورد نظر یافت نشد')
    context={
        'title':'نمایش دانشجویان بر حسب ترم',
        'studnt_term':studnt_term
    }
    return render(request,'college/show_student_by_studnt_term.html',context)

def show_student_payment_history(request,*args,**kwargs):
    student_id=kwargs['studentId']
    payment=models.Payment.objects.get_by_id(student_id)
    if payment is None:
        raise Http404('تاریخچه وجه دانشجو مورد نظر یافت نشد ')
    context={
        'title':'تاریچه دانشجو',
        'payment':payment
    }
    return render(request,'college/show_student_payment_history.html',context)



def show_teacher_payment_history(request,*args,**kwargs):
    teacher_id=kwargs['teacherId']
    teacher_payment=models.TeacherPayment.objects.get_by_id(teacher_id)
    if teacher_payment is None:
        raise Http404('تاریخچه وجه استاد مورد نظر یافت نشد ')
    context={
        'title':'تاریخچه پرداخت استاد',
        'teacher_payment':teacher_payment
    }
    return render(request,'college/show_teacher_payment_history.html',context)
    

# def show_student_payment(request,*args,**kwargs):
#     student_id=kwargs['studentId']
#     payment=models.Payment.objects.filter(student_id=student_id)
#     if payment is None:
#         raise Http404('تاریخچه وجه دانشجو مورد نظر یافت نشد')
#     context={
#         'title':'تاریخچه پرداخت وجه دانشجو',
#         'payment':payment
#     }
#     return render(request,'college/show_student_payment.html',context)

def show_student_education_history_info(request,*args,**kwargs):
    student_id=kwargs['studentId']
    student_term=models.StudentTerm.objects.get_by_id(student_id)
    if student_term is None:
        raise Http404('ترم دانشجو مورد نظر یافت نشد')
    context={
        'title':'تاریخچه تحصیلی دانشجو',
        'student_term':student_term
    }
    return render(request,'college/show_student_education_history_info.html',context)

def show_teacher_info(request,*args,**kwargs):
    teacher_id=kwargs['teachertId']
    teacher=models.Teacher.objects.get_by_id(teacher_id)
    if teacher is None:
        raise Http404('استاد مورد نظر یافت نشد')
    context={
        'title':'اطلاعات استاد',
        'teacher':teacher
    }
    return render(request,'college/show_teacher_info.html',context)

def edit_student_info(request, student_id):
    student = get_object_or_404(models.Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm(instance=student)
    context={
        'title':'ویرایش اطلاعات دانشجو',
        'form': form, 
        'student': student
    }
    return render(request, 'college/edit_student_info.html', context)

def edit_teacher_info(request, teacher_id):
    teacher = get_object_or_404(models.Teacher, id=teacher_id)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
    else:
        form = TeacherForm(instance=teacher)
    context={
        'title':'ویرایش اطلاعات استاد',
        'form': form, 
        'student': teacher
    }
    return render(request, 'college/edit_teacher_info.html',context)