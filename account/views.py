from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


from .forms import login_form,register_form

# Create your views here.

""" login view """
def login_view(request):
    form = login_form(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    context={
        'form':form
    }
    return render(request,'account/login_page.html',context)

""" register view """
def register_view(request):
    form = register_form(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('Username')
        email = form.cleaned_data.get('email')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('Password')
        User.objects.create_user(
            username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        return redirect('/account/login')
    context={
        'form':form
    }
    return render(request,'account/register_page.html',context)