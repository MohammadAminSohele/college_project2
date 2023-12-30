from django.shortcuts import render, redirect
from .forms import StudentForm,StudentTermForm,TeacherForm,TeacherTermForm

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