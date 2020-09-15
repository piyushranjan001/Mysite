from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):

    
    my_dict = {'insert_me':"Hello i am from views.py !"}
    return render(request, 'first_app/home.html', my_dict)  
    
def removepunc(request):

    # text analyzer 
    textwala = (request.GET.get('text','default'))
    checkwala = (request.GET.get('check','off'))
    passwala = (request.GET.get('pass','default'))
    

    if checkwala == "on":
        punctuations = "!@#$%^&*()_.,;:'\}{[]`"
        analyzed = " "
        for char in textwala:
            if char not in punctuations:
                analyzed = analyzed + char
                
        
        params = {'analyzed_text':analyzed}
        return render(request,'first_app/submit.html',params)
    
    
    else:
        return HttpResponse("Error")
