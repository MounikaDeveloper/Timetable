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
    x=Registration.objects.filter(username=uname,password=password)
    if x:
            request.session['uname'] = uname
            return render(request,"timetable.html",{"message":request.session['uname']})
    else:
        return render(request, "login.html",{"message":"Invalid Login Details"})


def timeTable(request):
    try:
        uname=request.session['uname']
        return render(request,"timetable.html",{"session":uname})
    except KeyError:
        return render(request, "timetable.html", {"message": "please login"})

def logout(request):
    try:
        del request.session['uname']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

def timeTable1(request):
    return render(request,"timetable1.html")


def saveTable(request):
    day=request.POST.get("day")
    t1=request.POST.get("t1")
    t2=request.POST.get("t2")
    t3=request.POST.get("t3")
    print(day,t1)
    return None