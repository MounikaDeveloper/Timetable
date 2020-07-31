from django.http import HttpResponse
from django.shortcuts import render
from app.models import Registration, TimetableModel
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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
            return render(request,"timetable1.html")
    else:
        return render(request, "login.html",{"message":"Invalid Login Details"})




def logout(request):
    try:
        del request.session['uname']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

def timeTable1(request):
    try:
        uname=request.session['uname']
        return render(request,"timetable1.html")
    except KeyError:
        return render(request, "timetable1.html", {"message": "please login"})


@csrf_exempt
def saveTable(request):
    uname=request.session['uname']
    weekname = request.POST["day"]
    t1 = request.POST["t1"]
    t2   = request.POST["t2"]
    t3 = request.POST["t3"]
    t4= request.POST["t4"]
    t5 = request.POST["t5"]
    t6 = request.POST["t6"]
    t7 = request.POST["t7"]
    t8 = request.POST["t8"]
    TimetableModel(username=uname,weekname=weekname,t1=t1,t2=t2,t3=t3,t4=t4,t5=t5,t6=t6,t7=t7,t8=t8).save()
    data=TimetableModel.objects.filter(username=uname)
    return render(request,"viewtable.html",{"data":data})


def viewTable(request):
    uname = request.session['uname']
    data = TimetableModel.objects.filter(username=uname)
    return render(request, "viewtable.html", {"data": data})