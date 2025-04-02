from django.shortcuts import render,redirect
from Administrator.models import *
from User.models import *
from django.http import JsonResponse
import json
from datetime import time, datetime, timedelta, date
from django.db.models import Sum
from io import BytesIO
import base64
from django.db.models import Count

def Homepage(request):
    if request.method=="POST":
        return redirect(request,"User/Homepage.html")
    else:
        return render(request,'User/Homepage.html')
def myprofile(request):
    studentreg=tbl_studentreg.objects.get(id=request.session['sid'])
    return render(request,"User/Myprofile.html",{'studentreg':studentreg})
def editprofile(request):
    studentreg=tbl_studentreg.objects.get(id=request.session['sid'])
    if request.method=="POST":
        studentreg.studentreg_name=request.POST.get("txt_name")
        studentreg.studentreg_email=request.POST.get("txt_email")
        studentreg.studentreg_contact=request.POST.get("txtcontact")
        if request.FILES.get("file_doc"):
            studentreg.studentreg_photo=request.FILES.get("file_doc")
        studentreg.save()
        return redirect("User:myprofile")
    else:
        return render(request,"User/Editprofile.html",{'edit':studentreg})
def changepassword(request):
    studentreg=tbl_studentreg.objects.get(id=request.session['sid'])
    dbpass=studentreg.studentreg_password
    if request.method == "POST":
        oldpassword=request.POST.get("txt_opass")
        newpassword=request.POST.get("txt_npass")
        cpassword=request.POST.get("txt_cpass")
        if dbpass==oldpassword:
            if newpassword==cpassword:
                studentreg.studentreg_password=newpassword
                studentreg.save()
                return render(request,"User/Changepassword.html",{"msg1":"Password Updated"})
            else:
                return render(request,"User/Changepassword.html",{"msg":"Password Mismatch"})
        else:
            return render(request,"User/Changepassword.html",{"msg":"Incorrect Password "})
    else:
        return render(request,"User/Changepassword.html")
def viewjobpost(request):
    data=tbl_jobpost.objects.all()
    return render(request,'User/viewjobpost.html',{'data':data})
def complaint(request):
    data=tbl_complaint.objects.filter(student=request.session['sid'])
    if request.method=="POST":
        content=request.POST.get('txt_comp')
        tbl_complaint.objects.create(
            complaint_content=content,
            student=tbl_studentreg.objects.get(id=request.session['sid'])
        )
        return render(request,'User/Complaint.html',{'data':data})
    else:
        return render(request,'User/Complaint.html',{'data':data})
def jobpost(request):
    user=tbl_studentreg.objects.get(id=request.session['sid'])
    cgpa=user.studentreg_cgpa
    backlog=user.studentreg_backlog
    department=user.department
    data=tbl_jobpost.objects.filter(tbl_jobpostdepartment__department=department,jobpost_mincgpa__lte=cgpa,jobpost_backlog__lte=backlog)
    return render(request,'User/Viewjobpost.html',{'data':data})
def requestjob(request,id):
    tbl_jobrequest.objects.create(
        jobpost=tbl_jobpost.objects.get(id=id),
        student=tbl_studentreg.objects.get(id=request.session['sid']))
    return redirect("User:viewjobpost")

def notification(request):
    student = tbl_studentreg.objects.get(id=request.session["sid"])
    jobpost = tbl_jobpost.objects.filter(jobpost_mincgpa__lte=student.studentreg_cgpa,tbl_jobpostdepartment__department=student.department.id,jobpost_backlog__lte=student.studentreg_backlog)
    return render(request,"User/Notification.html",{"notification":jobpost})


def viewexam(request):
    user = tbl_studentreg.objects.get(id=request.session["sid"])
    exam = tbl_examination.objects.filter(department=user.department.id,examination_status__gt=0)
    for i in exam:
        exambodycount = tbl_examinationbody.objects.filter(examination=i.id,student=request.session["sid"],examinationbody_status=1).count()
        if exambodycount > 0:
            i.examstatus = 1
    return render(request,"User/ViewExam.html",{'exam':exam})

def viewquestion(request,id):
    question = tbl_questions.objects.filter(examination=id)
    optioncount = 0
    for i in question:
        count = tbl_options.objects.filter(questions=i.id).count()
        if count > 0:
            optioncount = optioncount + 1
    examcount = tbl_examinationbody.objects.filter(examination=id,student=request.session["sid"]).count()
    if examcount > 0:
        exambodyid = tbl_examinationbody.objects.get(examination=id,student=request.session["sid"])
        return render(request,"User/ViewQuestion.html",{'questions':question,"exambodyid":exambodyid.id,"optioncount":optioncount,"examination_id":id})
    else:
        exambodyid = tbl_examinationbody.objects.create(student=tbl_studentreg.objects.get(id=request.session["sid"]),examination=tbl_examination.objects.get(id=id))
        return render(request,"User/ViewQuestion.html",{'questions':question,"exambodyid":exambodyid.id,"optioncount":optioncount,"examination_id":id})

def ajaxexamanswer(request):
    exam_answer = request.GET.get('answers')
    answers_dict = json.loads(exam_answer)
    for question_key, option_id in answers_dict.items():
        questionid = question_key.split("_")[1]
        options = tbl_options.objects.get(questions=questionid,status=True)
        if option_id == None:
            tbl_examinationanswers.objects.create(examinationbody=tbl_examinationbody.objects.get(id=request.GET.get('exambodyid')),question=tbl_questions.objects.get(id=questionid),correct_answer=tbl_options.objects.get(id=options.id))
        else:
            tbl_examinationanswers.objects.create(examinationbody=tbl_examinationbody.objects.get(id=request.GET.get('exambodyid')),question=tbl_questions.objects.get(id=questionid),myanswer=tbl_options.objects.get(id=option_id),correct_answer=tbl_options.objects.get(id=options.id))
    exambody = tbl_examinationbody.objects.get(id=request.GET.get('exambodyid'))
    exambody.examinationbody_status = 1
    exambody.save()
    return JsonResponse({"msg":"Examination Submitted Sucessfully..."})

def ajaxtimer(request):
    exam = tbl_examination.objects.get(id=request.GET.get('exam'))
    timecount = tbl_timmer.objects.filter(exam=exam).count()
    if timecount > 0:
        timer_obj = tbl_timmer.objects.get(exam=exam)
        if timer_obj.timmer > time(0, 0, 0):
            current_datetime = datetime.combine(datetime.today(), timer_obj.timmer)
            new_datetime = current_datetime - timedelta(seconds=1)
            new_time = new_datetime.time()
            timer_obj.timmer = new_time
            timer_obj.save()
            time_str = new_time.strftime("%H:%M:%S")
            return JsonResponse({"msg": time_str,"status":False})
        else:
            exam.examination_status = 2
            exam.save()
            return JsonResponse({"msg": "Time's up","status":True})
    else:
        tbl_timmer.objects.create(exam=exam,timmer=exam.time)
        return JsonResponse({"msg": ""})

def successer(request):
    return render(request,"User/Success.html")

def viewresult(request, id):
    result = tbl_examinationanswers.objects.filter(examinationbody__examination=id,examinationbody__student=request.session["sid"],examinationbody__examinationbody_status=1)
    question = tbl_questions.objects.filter(examination=id).count()
    if result[0].examinationbody.total_marks == 0:
        total = 0
        for i in result:
            if i.myanswer and i.myanswer.id == i.correct_answer.id:
                total += 1
        exambody = tbl_examinationbody.objects.get(examination=id,student=request.session["sid"],examinationbody_status=1)
        exambody.total_marks = total
        exambody.save()
    return render(request,"User/viewResult.html",{"result": result,"question":question})

def chart(request):
    return render(request, 'User/Chart.html')

def department_chart_data(request):
    departments = tbl_department.objects.all()
    placement = []
    dates = date.today()
    for i in departments:
        count = tbl_jobrequest.objects.filter(student__department=i.id,status=1,date__year=dates.year).count()
        placement.append(count)
    department_names = [dept.department_name for dept in departments]

    return JsonResponse({
        "labels": department_names,
        "data": placement
    })

def examnotification(request):
    user = tbl_studentreg.objects.get(id=request.session["sid"])
    exam = tbl_examination.objects.filter(department=user.department.id,examination_status=0)
    return render(request,"User/ExaminationNotification.html",{'exam':exam})