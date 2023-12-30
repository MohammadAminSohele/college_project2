from django.shortcuts import render, redirect
from django.views.generic import ListView


from .forms import StudentForm,StudentTermForm,TeacherForm,TeacherTermForm
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
    return render(request, 'college/register_student.html', {'form': form})


def register_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TeacherForm()
    return render(request, 'college/register_teacher.html', {'form': form})


def add_student_term(request):
    if request.method == 'POST':
        form = StudentTermForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page
    else:
        form = StudentTermForm()

    return render(request, 'college/add_student_term.html', {'form': form})


def add_teacher_term(request):
    if request.method == 'POST':
        form = TeacherTermForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page
    else:
        form = TeacherTermForm()

    return render(request, 'college/add_teacher_term.html', {'form': form})


def show_students_info(request):
    students=models.Student.objects.all().values('nat_code','first_name','last_name')
    context={
        'students':students
    }
    return render(request,'college/show_students_info.html',context)

class search_student_list(ListView):
    template_name = 'college/search-student-list.html'

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return models.Student.objects.search(query)
        return models.Student.objects.all().values('nat_code','first_name','last_name')


def show_student_info(request):
    context={

    }
    return render(request,'college/show_student_info.html',context)