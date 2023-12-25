from django.shortcuts import render

# Create your views here.

""" login view """
def login_view(request):
    return render(request,'account/login_page.html',{})