from django.shortcuts import render,redirect
from Administrator.models import *
from User.models import *
from datetime import date
from django.http import JsonResponse


def myprofile(request):
    hod=tbl_hod.objects.get(id=request.session['hid'])
    return render(request,"Hod/Myprofile.html",{'hod':hod})
def Homepage(request):
    return render(request,'Hod/Homepage.html')

def get_bar_chart(request):
    placement = []
    y = []
    hod=tbl_hod.objects.get(id=request.session['hid'])
    dept = tbl_department.objects.get(id=hod.department.id)
    for i in range(0,4):
        dates = date.today()
        year = dates.year - int(i)
        y.append(year)
        count = tbl_jobrequest.objects.filter(student__department=hod.department.id,status=1,date__year=year).count()
        placement.append(count)
    y.reverse()
    placement.reverse()
    return JsonResponse({
        "labels": y,
        "data": placement
    })

def editprofile(request):
    hod=tbl_hod.objects.get(id=request.session['hid'])
    if request.method=="POST":
        hod.hod_name=request.POST.get("txt_name")
        hod.hod_email=request.POST.get("txt_email")
        hod.hod_contact=request.POST.get("txtcontact")
        hod.save()
        return redirect("Hod:myprofile")
    else:
        return render(request,"Hod/Editprofile.html",{'edit':hod})
def changepassword(request):
    hod=tbl_hod.objects.get(id=request.session['hid'])
    dbpass=hod.hod_password
    if request.method == "POST":
        oldpassword=request.POST.get("txt_opass")
        newpassword=request.POST.get("txt_npass")
        cpassword=request.POST.get("txt_cpass")
        if dbpass==oldpassword:
            if newpassword==cpassword:
                hod.hod_password=newpassword
                hod.save()
                return render(request,"Hod/Changepassword.html",{"msg1":"Password Updated"})
            else:
                return render(request,"Hod/Changepassword.html",{"msg":"Password Mismatch"})
        else:
            return render(request,"Hod/Changepassword.html",{"msg":"Incorrect Password "})
    else:
        return render(request,"Hod/Changepassword.html")
def notification(request):
    notification = tbl_notification.objects.all()
    return render(request,"Hod/Notification.html",{"notification":notification})
def studentlist(request):
    data=tbl_studentreg.objects.filter(department=request.session['dept'])
    return render(request,'Hod/Studentlist.html',{'data':data})
def confirmlist(request):
    data=tbl_jobrequest.objects.filter(jobpost__department=request.session['dept'])
    return render(request,'Hod/Confirmlist.html',{'data':data})
def placedlist(request):
    data=tbl_jobrequest.objects.filter(jobpost__department=request.session['dept'],status=1)
    return render(request,'Hod/Placedlist.html',{'data':data})
def viewjobs(request):
    data=tbl_jobpost.objects.filter(department=request.session['dept'])
    return render(request,'Hod/Joblist.html',{'data':data})
def eligiblelist(request,id):
    data=tbl_jobpost.objects.get(id=id)
    student=tbl_studentreg.objects.filter(studentreg_cgpa__gte=data.jobpost_mincgpa,studentreg_backlog__lte=data.jobpost_backlog,department=data.department)
    # print(student)
    return render(request,'Hod/Eligiblelist.html',{'student':student,'company':data})

def viewexam(request):
    exm=tbl_examination.objects.filter(examination_status=2)
    return render(request,"Hod/ViewExam.html",{"exam":exm})

def viewresult(request, id):
    user = tbl_studentreg.objects.filter(tbl_examinationbody__examination=id)
    return render(request, "Hod/ViewResult.html", {'user': user})