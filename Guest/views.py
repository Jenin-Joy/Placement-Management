from django.shortcuts import render,redirect
from Guest.models import *
from Administrator.models import *
from User.models import *
def UserRegistration(request):
    if request.method=="POST":
        if request.POST.get('txtpass')==request.POST.get('rpass'):
            tbl_user.objects.create(
                user_name=request.POST.get('txtname'),
                user_email=request.POST.get('txtemail'),
                user_password=request.POST.get('txtpass'),
                )
     
            return render(request,"Guest/UserRegistration.html",{'msg':"Registration Completed Successfully"})   
        else:
            return render(request,"Guest/UserRegistration.html",{'msg':"Password doesnot match."})   
    else:
        return render(request,"Guest/UserRegistration.html")
def Login(request):
     if request.method=="POST":
          email=request.POST.get("txtemail")
          password=request.POST.get("txtpass")
          admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
          hodcount=tbl_hod.objects.filter(hod_email=email,hod_password=password).count()
          studentcount=tbl_studentreg.objects.filter(studentreg_email=email,studentreg_password=password).count()
          alumnicount=tbl_alumnireg.objects.filter(alumnireg_email=email,alumnireg_password=password).count()
          if admincount>0:
            admin=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['uid']=admin.id
            return redirect("Admin:Homepage")
          elif hodcount>0:
            hod=tbl_hod.objects.get(hod_email=email,hod_password=password)
            request.session['hid']=hod.id
            request.session['dept']=hod.department.id
            return redirect("Hod:Homepage")
          elif studentcount>0:
            studentreg=tbl_studentreg.objects.get(studentreg_email=email,studentreg_password=password)
            request.session['sid']=studentreg.id
            return redirect("User:Homepage")
          elif alumnicount>0:
            alumnireg=tbl_alumnireg.objects.get(alumnireg_email=email,alumnireg_password=password)
            request.session['aid']=alumnireg.id
            return redirect("Alumni:Homepage")
          else:
               return render(request,"Guest/Login.html",{"msg":"Invalid Email Or Password"})
     else:
          return render(request,"Guest/Login.html")

def index(request):
    data=tbl_jobrequest.objects.filter(status=1)
    department = tbl_department.objects.all()
    return render(request,'Guest/index.html',{'data':data,"department":department})
def userdashboard(request):
    return render(request,'Guest/Userdashboard.html')

def department_chart_data(request):
    departments = tbl_department.objects.all()
    placement = []
    pre_placement = []
    dates = date.today()
    for i in departments:
        count = tbl_jobrequest.objects.filter(student__department=i.id,status=1,date__year=dates.year).count()
        placement.append(count)
    pre_year = dates.year - 1
    for i in departments:
        count = tbl_jobrequest.objects.filter(student__department=i.id,status=1,date__year=pre_year).count()
        pre_placement.append(count)
    department_names = [dept.department_name for dept in departments]

    return JsonResponse({
        "labels": department_names,
        "data": placement,
        "pre_data": pre_placement
    })