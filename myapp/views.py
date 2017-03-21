from django.shortcuts import render
from django.http import HttpResponse


def func(request):
    my_list = {'test_key':'Help page',}
    return render(request,'myapp/first_templates.html',context=my_list)



# Create your views here.
