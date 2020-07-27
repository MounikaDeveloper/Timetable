from django.http import HttpResponse
from django.shortcuts import render
from app.models import Registration

def showIndex(request):
    return render(request,'index.html')


def register(request):
    return render(request,'register.html')


def createForm(request):
    uname=request.POST.get("uname")
    password=request.POST.get("password")
    print(uname,password)
    try:
        Registration(username=uname,password=password).save()
    except:
        return render(request, 'register.html', {"message": "Username already exists please login"})
    return render(request,'register.html',{"message":"Registration was Successful"})


def login(request):
    return render(request,"login.html")


def userValidation(request):
    uname = request.POST.get("uname")
    password = request.POST.get("password")
    try:
        Registration.objects.get(username=uname,password=password)
        request.session['uname'] = uname
        return render(request,"timetable.html",{"message":request.session['uname']})
    except:
        return render(request, "login.html",{"message":"Invalid Login Details"})


def timeTable(request):
    return render(request,"timetable.html",)

def logout(request):
    try:
        del request.session['uname']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

def timeTable1(request):
    return render(request,"timetable1.html")


