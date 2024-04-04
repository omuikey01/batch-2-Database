from django.shortcuts import render
from .models import Student


# Create your views here.

def indexpage(request):
    return render(request, "index.html")

def datasavepage(request):
    if request.method == "POST":

        name = request.POST['nm']
        email = request.POST['em']
        claass = request.POST['class']
        gender = request.POST['gender']
        city = request.POST['ct']
        course = request.POST['course']
        fess = request.POST['fess']
        
        # print(namme, email, claass, gender,city,course,fess)
        Student.objects.create(name = name,
                               email = email,
                               claass = claass,
                               gender = gender,
                               city = city,
                               course = course,
                               fess = fess)
    else :
        print("********************************")
        print("Exit ")
        print("********************************")