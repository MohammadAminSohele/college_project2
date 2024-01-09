from django.shortcuts import render


def header(request, *args, **kwargs):
    context = {
        'title': 'this is title'
    }
    return render(request, 'shared/Header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    context = {
        "about_us": "این سایت فروشگاهی به وسیله ی django در سایت Topelarn ایجاد شده است"
    }
    return render(request, 'shared/Footer.html', context)

""" index view """
def index_view(request):
    return render(request,'home_page.html',{})