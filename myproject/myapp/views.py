from django.shortcuts import render

from django.http import HttpResponse 

def home(request):
   # return HttpResponse('hello,world. your welcome to django page')
   return render(request, 'website/index.html')

def about(request):
    #return HttpResponse('hello,world. your welcome to django about page')
    return render(request, 'website/about.html')
def contact(request):
    #return HttpResponse('hello,world. your welcome to django contact page')
    return render(request, 'website/contact.html')