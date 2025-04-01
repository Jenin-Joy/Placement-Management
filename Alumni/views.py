from django.shortcuts import render,redirect
from Administrator.models import *
def Homepage(request):
    if request.method=="POST":
        return redirect(request,"Alumni/Homepage.html")
    else:
        return render(request,'Alumni/Homepage.html')
def myprofile(request):
    alumnireg=tbl_alumnireg.objects.get(id=request.session['aid'])
    return render(request,"Alumni/Myprofile.html",{'alumnireg':alumnireg})
def editprofile(request):
    alumnireg=tbl_alumnireg.objects.get(id=request.session['aid'])
    if request.method=="POST":
        alumnireg.alumnireg_name=request.POST.get("txt_name")
        alumnireg.alumnireg_email=request.POST.get("txt_email")
        alumnireg.alumnireg_contact=request.POST.get("txtcontact")
        alumnireg.save()
        return redirect("Alumni:myprofile")
    else:
        return render(request,"Alumni/Editprofile.html",{'edit':alumnireg})
def changepassword(request):
    alumnireg=tbl_alumnireg.objects.get(id=request.session['aid'])
    dbpass=alumnireg.alumnireg_password
    if request.method == "POST":
        oldpassword=request.POST.get("txt_opass")
        newpassword=request.POST.get("txt_npass")
        cpassword=request.POST.get("txt_cpass")
        if dbpass==oldpassword:
            if newpassword==cpassword:
                alumnireg.alumnireg_password=newpassword
                alumnireg.save()
                return render(request,"Alumni/Changepassword.html",{"msg1":"Password Updated"})
            else:
                return render(request,"Alumni/Changepassword.html",{"msg":"Password Mismatch"})
        else:
            return render(request,"Alumni/Changepassword.html",{"msg":"Incorrect Password "})
    else:
        return render(request,"Alumni/Changepassword.html")
def jobpost(request):
    data=tbl_jobpost.objects.filter(alumini=request.session['aid'])
    department=tbl_department.objects.all()
    if request.method=="POST":
        companyname=request.POST.get('txt_companyname')
        details=request.POST.get('txt_details')
        mincgpa=request.POST.get('txt_mincgpa')
        jobpost_department = request.POST.getlist('sel_Dept[]')  
        backlog=request.POST.get('txtback')
        file_doc=request.FILES.get('file_doc')
        lastdate=request.POST.get('txt_lastdate')
        # department=tbl_department.objects.get(id=jobpost_department)
        job = tbl_jobpost.objects.create(
            jobpost_companyname=companyname,
            jobpost_details=details,
            jobpost_mincgpa=mincgpa,
            jobpost_backlog=backlog,
            jobpost_file_doc=file_doc,
            jobpost_lastdate=lastdate,
            alumini=tbl_alumnireg.objects.get(id=request.session['aid'])
        )
        for i in jobpost_department:
            tbl_jobpostdepartment.objects.create(
                department = tbl_department.objects.get(id=i),
                jobpost = tbl_jobpost.objects.get(id=job.id)
            )
        return redirect("Alumni:jobpost")
    else:
        return render(request,'Alumni/JobPost.html',{'data':data,'department':department})