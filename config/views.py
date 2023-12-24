from django.shortcuts import render

""" index view """
def index_view(request):
    return render(request,'index_page.html',{})