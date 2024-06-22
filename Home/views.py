from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    
    students = [
        {'name':'krutik', 'marks':46 },
        {'name':'bhavik', 'marks':76 },
        {'name':'vivek', 'marks':86 },
        {'name':'deep', 'marks':96 },
        {'name':'devli', 'marks':16 },
        {'name':'devlo', 'marks':56 }, 
                ]
    return render(request , "index.html", context={'students':students}) 