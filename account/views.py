from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login


from .forms import login_form

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