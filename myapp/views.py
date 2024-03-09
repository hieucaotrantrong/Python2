from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    response = HttpResponse()
    response.writelines("<h1>Hello Dong A University</h1>")
    response.writelines("this is home")
    return response


def index(request):
    return render(request, "page/home.html")
