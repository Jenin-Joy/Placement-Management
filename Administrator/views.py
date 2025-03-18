from django.shortcuts import render,redirect
from Administrator.models import *
from User.models import *
from django.core.exceptions import ValidationError
from django.contrib import messages
import pandas as pd
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime

def adminreg(request):
    data=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_pass')
        tbl_admin.objects.create(
            admin_name=name,
            admin_email=email,
            admin_password=password
        )
        return render(request,'Administrator/Adminreg.html')
    else:
        return render(request,'Administrator/Adminreg.html',{'data':data})
def Homepage(request):
    return render(request,'Administrator/Homepage.html')
def studentmanagement(request):
    return render(request,'Administrator/Studentmanagement.html')
def studentreg(request):
     data=tbl_studentreg.objects.all()
     department=tbl_department.objects.all()
     academicyear=tbl_academicyear.objects.all()
     semester=tbl_semester.objects.all()
     if request.method=="POST":
        studentreg_ktuid=request.POST.get('txt_ktuid')
        studentreg_name=request.POST.get('txt_name')
        studentreg_email=request.POST.get('txt_email')
        studentreg_contact=request.POST.get('txtcontact')
        studentreg_department=request.POST.get('sel_Dept')
        studentreg_academicyear=request.POST.get('sel_acad')
        studentreg_semester=request.POST.get('sel_sem')
        studentreg_cgpa=request.POST.get('txt_cgpa')
        studentreg_backlog=request.POST.get('txtback')
        studentreg_dob=request.POST.get('txt_date')
        studentreg_password=request.POST.get('txt_pass')
        department=tbl_department.objects.get(id=studentreg_department)
        academicyear=tbl_academicyear.objects.get(id=studentreg_academicyear)
        semester=tbl_semester.objects.get(id=studentreg_semester)
        tbl_studentreg.objects.create(
            studentreg_ktuid=studentreg_ktuid,
            studentreg_name=studentreg_name,
            studentreg_email=studentreg_email,
            studentreg_contact=studentreg_contact,
            department=department,
            academicyear=academicyear,
            semester=semester,
            studentreg_cgpa=studentreg_cgpa,
            studentreg_backlog=studentreg_backlog,
            studentreg_dob=studentreg_dob,
            studentreg_password=studentreg_password,
            )
        return render(request,'Administrator/Studentreg.html',{'msg':"Student Registration Completed.."})
     else:
        return render(request,'Administrator/Studentreg.html',{'data':data,'department':department,'academicyear':academicyear,'semester':semester})
def alumnireg(request):
     data=tbl_alumnireg.objects.all()
     department=tbl_department.objects.all()
     academicyear=tbl_academicyear.objects.all()
     if request.method=="POST":
        alumnireg_name=request.POST.get('txt_name')
        alumnireg_email=request.POST.get('txt_email')
        alumnireg_contact=request.POST.get('txtcontact')
        alumnireg_department=request.POST.get('sel_Dept')
        alumnireg_academicyear=request.POST.get('sel_acad')
        alumnireg_dob=request.POST.get('txt_date')
        alumnireg_password=request.POST.get('txt_pass')
        department=tbl_department.objects.get(id=alumnireg_department)
        academicyear=tbl_academicyear.objects.get(id=alumnireg_academicyear)
        tbl_alumnireg.objects.create(
            alumnireg_name=alumnireg_name,
            alumnireg_email=alumnireg_email,
            alumnireg_contact=alumnireg_contact,
            department=department,
            academicyear=academicyear,
            alumnireg_dob=alumnireg_dob,
            alumnireg_password=alumnireg_password,
            )
        return render(request,'Administrator/Alumnireg.html',{'msg':"Alumni Registration Completed.."})
     else:
        return render(request,'Administrator/Alumnireg.html',{'data':data,'department':department,'academicyear':academicyear})
def department(request):
    data=tbl_department.objects.all()
    if request.method=="POST":
        department=request.POST.get('txt_dep')
        tbl_department.objects.create(
            department_name=department,
        )
        return render(request,'Administrator/Department.html',{'data':data})
    else:
        return render(request,'Administrator/Department.html',{'data':data})
def deletedepartment(request,id):
    tbl_department.objects.get(id=id).delete()
    return redirect("Admin:department")
def editdepartment(request,id):
    ed=tbl_department.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("txt_dep")
        ed.department_name=name
        ed.save()
        return redirect("Admin:department")
    else:
        return render(request,"Administrator/Department.html",{'edit':ed})
def academicyear(request):
    data=tbl_academicyear.objects.all()
    if request.method=="POST":
        academicyear=request.POST.get('txt_acad')
        tbl_academicyear.objects.create(
            academicyear_name=academicyear,
        )
        return render(request,'Administrator/AcademicYear.html',{'data':data})
    else:
        return render(request,'Administrator/AcademicYear.html',{'data':data})
def deletedacademicyear(request,id):
    tbl_academicyear.objects.get(id=id).delete()
    return redirect("Admin:academicyear")
def editacademicyear(request,id):
    ed=tbl_academicyear.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("txt_acad")
        ed.academicyear_name=name
        ed.save()
        return redirect("Admin:academicyear")
    else:
        return render(request,"Administrator/AcademicYear.html",{'edit':ed})
def semester(request):
    data=tbl_semester.objects.all()
    if request.method=="POST":
        semester=request.POST.get('txt_sem')
        tbl_semester.objects.create(
            semester_name=semester,
        )
        return redirect("Admin:semester")
    else:
        return render(request,'Administrator/Semester.html',{'data':data})
def deletesemester(request,id):
    tbl_semester.objects.get(id=id).delete()
    return redirect("Admin:semester")
def editsemester(request,id):
    ed=tbl_semester.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("txt_sem")
        ed.semester_name=name
        ed.save()
        return redirect("Admin:semester")
    else:
        return render(request,"Administrator/Semester.html",{'edit':ed})
def examtype(request):
    data=tbl_examtype.objects.all()
    if request.method=="POST":
        examtype=request.POST.get('txt_exam')
        tbl_examtype.objects.create(
            examtype_name=examtype,
        )
        return render(request,'Administrator/Examtype.html',{'data':data})
    else:
        return render(request,'Administrator/Examtype.html',{'data':data})
def deletedexamtype(request,id):
    tbl_examtype.objects.get(id=id).delete()
    return redirect("Admin:examtype")
def editexamtype(request,id):
    ed=tbl_examtype.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("txt_exam")
        ed.examtype_name=name
        ed.save()
        return redirect("Admin:examtype")
    else:
        return render(request,"Administrator/Examtype.html",{'edit':ed})
def studentlist(request):
    data=tbl_studentreg.objects.all()
    return render(request,'Administrator/StudentList.html',{'data':data})
def jobpost(request):
    alumini = tbl_alumnireg.objects.all()
    data = tbl_jobpost.objects.filter().exclude(alumini__in=alumini)
    department=tbl_department.objects.all()
    
    if request.method == "POST":
        companyname = request.POST.get('txt_companyname')
        details = request.POST.get('txt_details')
        mincgpa = float(request.POST.get('txt_mincgpa'))
        jobpost_department = request.POST.get('sel_Dept')  
        backlog = request.POST.get('txtback')  
        file_doc = request.POST.get('file_doc')
        lastdate = request.POST.get('txt_lastdate')
        department=tbl_department.objects.get(id=jobpost_department)
        # Create the job post
        tbl_jobpost.objects.create(
            jobpost_companyname=companyname,
            jobpost_details=details,
            jobpost_mincgpa=mincgpa,
            department=department,
            jobpost_backlog=backlog,
            jobpost_file_doc=file_doc,
            jobpost_lastdate=lastdate,
        )
        
        # Get eligible students (CGPA >= mincgpa and no backlogs)
        eligible_students = tbl_studentreg.objects.filter(
            studentreg_cgpa__gte=mincgpa,  # Greater than or equal to min CGPA
            studentreg_backlog__lte= backlog ,# Assuming '0' means no backlogs
            department= department
        )
        
        # Prepare email content
        subject = f'New Job Opportunity at {companyname}'
        message = (
            "Dear Student,\n\n"
            f"A new job opportunity has been posted that matches your profile:\n\n"
            f"Company: {companyname}\n"
            f"Details: {details}\n"
            f"Minimum CGPA Required: {mincgpa}\n"
            f"Department: {department.department_name}\n"
            f"Backlog Limit: {backlog}\n"
            f"Last Date to Apply: {lastdate}\n\n"
            "Please check the attached document (if any) and apply before the deadline.\n"
            "For more details, login to your student portal.\n\n"
            "Best Regards,\n"
            "Placement Cell"
        )
        
        # Send email to all eligible students
        for student in eligible_students:
            email=student.studentreg_email
            # print(email)
            
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email]
            )
        
        return render(request, 'Administrator/JobPost.html',{'data':data})
    else:
        return render(request, 'Administrator/JobPost.html',{'data':data,'department':department})




def deletedjobpost(request,id):
    tbl_jobpost.objects.get(id=id).delete()
    return redirect("Admin:jobpost")
def viewalumni(request):
    data=tbl_alumnireg.objects.all()
    return render(request,'Administrator/ViewAlumni.html',{'data':data})
def viewalumnijobs(request,id):
    data=tbl_jobpost.objects.filter(alumini=id)
    return render(request,'Administrator/ViewAlumnijobs.html',{'data':data,"id":id})
def addhod(request):
    department=tbl_department.objects.all()
    return render(request,'Administrator/Addhod.html',{'department':department})
def addstudent(request):
    department=tbl_department.objects.all()
    academicyear=tbl_academicyear.objects.all()
    return render(request,'Administrator/Addstudent.html',{'department':department,'academicyear':academicyear})
def hod(request):
     data=tbl_hod.objects.all()
     department=tbl_department.objects.all()
     if request.method=="POST":
        hod_name=request.POST.get('txt_name')
        hod_email=request.POST.get('txt_email')
        hod_contact=request.POST.get('txtcontact')
        hod_department=request.POST.get('sel_Dept')
        hod_dob=request.POST.get('txt_date')
        hod_password=request.POST.get('txt_pass')
        department=tbl_department.objects.get(id=hod_department)
        tbl_hod.objects.create(
            hod_name=hod_name,
            hod_email=hod_email,
            hod_contact=hod_contact,
            department=department,
            hod_dob=hod_dob,
            hod_password=hod_password,
        )
        return render(request,'Administrator/Hod.html',{'msg':"HOD Registration Completed.."})
     else:
        return render(request,'Administrator/Hod.html',{'data':data,'department':department})
def hodlist(request):
    data=tbl_hod.objects.all()
    return render(request,'Administrator/HodList.html',{'data':data})
def viewcomplaint(request):
    data=tbl_complaint.objects.filter(status=0)
    replied=tbl_complaint.objects.filter(status=1)
    return render(request,'Administrator/Viewcomplaint.html',{'data':data,'replied':replied})
def reply(request,id):
    data=tbl_complaint.objects.get(id=id)
    if request.method=="POST":
        reply=request.POST.get('txt_reply')
        data.complaint_reply=reply
        data.status=1
        data.save()
        return redirect("Admin:viewcomplaint")
    else:
        return render(request,'Administrator/Reply.html')


def upload_excel(request):
    department=tbl_department.objects.all()
    year=tbl_academicyear.objects.all()
    semester=tbl_semester.objects.all()
    if request.method == "POST" and request.FILES.get("file_doc"):
        file = request.FILES["file_doc"]

        # Validate file type
        if not (file.name.endswith('.xlsx') or file.name.endswith('.xls')):
            messages.error(request, "Invalid file format! Only .xlsx or .xls files are allowed.")
            return render(request, "Administrator/StudentExcel.html")

        try:
            df = pd.read_excel(file)

            # Clean column names
            df.columns = df.columns.str.strip()
            # print(df.columns)

            # Required columns check
            required_columns = {"KTUID","NAME", "EMAIL", "CONTACT","CGPA", "BACKLOG", "DOB"}
            if not required_columns.issubset(df.columns):
                d=df.columns
                missing_columns = required_columns - set(df.columns)
                messages.error(request, f"Invalid Excel format! Missing required columns: {', '.join(missing_columns)}")
                return render(request, "Administrator/StudentExcel.html",{'data':d})
            for _, row in df.iterrows():
                
                KTUid, name, email, contact,cgpa, backlog,dob = row["KTUID"], row["NAME"], row["EMAIL"], row["CONTACT"],row["CGPA"],row["BACKLOG"],row["DOB"]
                password = name[:4] + str(dob.year) 
                # print(name)

                # Validate email format
                if "@" not in str(email):
                    messages.error(request, f"Invalid email: {email}")
                    continue  # Skip this record

                # Validate phone number (assuming a 10-digit format)
                if not str(contact).isdigit() or len(str(contact)) != 10:
                    messages.error(request, f"Invalid contact number: {contact}")
                    continue

                # Prevent duplicate emails
                # if not tbl_studentreg.objects.filter(studentreg_email=email).exists():
                tbl_studentreg.objects.create(
                    studentreg_ktuid=KTUid, studentreg_name=name, studentreg_email=email, studentreg_contact=contact,studentreg_dob=dob,studentreg_cgpa=cgpa, studentreg_backlog=backlog,
                    academicyear=tbl_academicyear.objects.get(id=request.POST.get("sel_acad")),department=tbl_department.objects.get(id=request.POST.get("sel_Dept")),semester=tbl_semester.objects.get(id=request.POST.get("sel_sem")),
                    studentreg_password=password,studentreg_photo="Assets/User/profile.jpg"
                )

            messages.success(request, "File uploaded and data saved successfully!")
            print(messages)

        except Exception as e:
            print(e)
            messages.error(request, f"Error processing file: {str(e)}")

    return render(request, "Administrator/StudentExcel.html",{'year':year,'department':department,'semester':semester})
def myprofile(request):
    admin=tbl_admin.objects.get(id=request.session['uid'])
    return render(request,"Administrator/Myprofile.html",{'admin':admin})
def editprofile(request):
    admin=tbl_admin.objects.get(id=request.session['uid'])
    if request.method=="POST":
        admin.admin_name=request.POST.get("txt_name")
        admin.admin_email=request.POST.get("txt_email")
        admin.save()
        return redirect("Admin:myprofile")
    else:
        return render(request,"Administrator/Editprofile.html",{'edit':admin})
def changepassword(request):
    admin=tbl_admin.objects.get(id=request.session['uid'])
    dbpass=admin.admin_password
    if request.method == "POST":
        oldpassword=request.POST.get("txt_opass")
        newpassword=request.POST.get("txt_npass")
        cpassword=request.POST.get("txt_cpass")
        if dbpass==oldpassword:
            if newpassword==cpassword:
                admin.admin_password=newpassword
                admin.save()
                return render(request,"Administrator/Changepassword.html",{"msg1":"Password Updated"})
            else:
                return render(request,"Administrator/Changepassword.html",{"msg":"Password Mismatch"})
        else:
            return render(request,"Administrator/Changepassword.html",{"msg":"Incorrect Password "})
    else:
        return render(request,"Administrator/Changepassword.html")
def editstudent(request,id):
    department=tbl_department.objects.all()
    academicyear=tbl_academicyear.objects.all()
    semester=tbl_semester.objects.all()
    ed=tbl_studentreg.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("txt_name")
        ed.studentreg_name=name
        email=request.POST.get("txt_email")
        ed.studentreg_email=email
        contact=request.POST.get("txtcontact")
        ed.studentreg_contact=contact
        cgpa=request.POST.get("txt_cgpa")
        ed.studentreg_cgpa=cgpa
        backlog=request.POST.get("txtback")
        ed.studentreg_backlog=backlog
        dob=request.POST.get("txt_date")
        # ed.studentreg_dob=dob
        ed.department=tbl_department.objects.get(id=request.POST.get("sel_Dept"))
        ed.academicyear=tbl_academicyear.objects.get(id=request.POST.get("sel_acad"))
        ed.semester=tbl_semester.objects.get(id=request.POST.get("sel_sem"))
        ed.save()
        return redirect("Admin:studentlist")
    else:
        return render(request,"Administrator/Studentreg.html",{'edit':ed,'department':department,'academicyear':academicyear,'semester':semester})
def notification(request):
    data=tbl_notification.objects.all()
    if request.method=="POST":
        notification=request.POST.get('txt_not')
        limit=request.POST.get('txt_lim')
        tbl_notification.objects.create(
            notification_notification=notification,
            notification_limit=limit,
        )
        return render(request,'Administrator/Notification.html',{'data':data})
    else:
        return render(request,'Administrator/Notification.html',{'data':data})
def deletenotification(request,id):
    tbl_notification.objects.get(id=id).delete()
    return redirect("Admin:notification")
def viewjobrequest(request):
    data=tbl_jobrequest.objects.all()
    return render(request,'Administrator/Viewjobrequest.html',{'data':data})
def deletestudent(request,id):
    tbl_studentreg.objects.get(id=id).delete()
    return redirect("Admin:studentlist")    
def jobmanagement(request):
    return render(request,'Administrator/Jobmanagement.html')
def acceptjob(request,id):
    data=tbl_jobrequest.objects.get(id=id)
    data.status=1
    data.save()
    return redirect("Admin:viewjobrequest")
def acceptlist(request):
    data=tbl_jobrequest.objects.filter(status=1)
    return render(request,'Administrator/Placedlist.html',{'data':data})
def rejectjob(request,id):
    data=tbl_jobrequest.objects.get(id=id)
    data.status=2
    data.save()

    return redirect("Admin:viewjobrequest")
def rejectlist(request):
    data=tbl_jobrequest.objects.filter(status=2)
    return render(request,'Administrator/Rejectedlist.html',{'data':data})
def eligiblelist(request,id):
    data=tbl_jobpost.objects.get(id=id)
    student=tbl_studentreg.objects.filter(studentreg_cgpa__gte=data.jobpost_mincgpa,studentreg_backlog__lte=data.jobpost_backlog,department=data.department)
    # print(student)
    return render(request,'Administrator/Eligiblelist.html',{'student':student,'company':data})
def verifylist(request,id):
    data=tbl_jobpost.objects.get(id=id)
    companyname = data.jobpost_companyname
    details = data.jobpost_details
    mincgpa = data.jobpost_mincgpa
    jobpost_department = data.department.department_name
    backlog = data.jobpost_backlog
    file_doc = data.jobpost_file_doc
    lastdate = data.jobpost_lastdate

    eligible_students = tbl_studentreg.objects.filter(
            studentreg_cgpa__gte=mincgpa,  # Greater than or equal to min CGPA
            studentreg_backlog__lte= backlog ,# Assuming '0' means no backlogs
            department= data.department.id
        )
    

    data.jobpost_status=1
    data.save()
    subject = f'New Job Opportunity at {companyname}'
    message = (
        "Dear Student,\n\n"
        f"A new job opportunity has been posted that matches your profile:\n\n"
        f"Company: {companyname}\n"
        f"Details: {details}\n"
        f"Minimum CGPA Required: {mincgpa}\n"
        f"Department: {jobpost_department}\n"
        f"Backlog Limit: {backlog}\n"
        f"Last Date to Apply: {lastdate}\n\n"
        "Please check the attached document (if any) and apply before the deadline.\n"
        "For more details, login to your student portal.\n\n"
        "Best Regards,\n"
        "Placement Cell"
    )
        
    # Send email to all eligible students
    for student in eligible_students:
        email=student.studentreg_email
        # print(email)
        
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email]
        )
    
    return render(request,'Administrator/ViewAlumnijobs.html',{'data':data})  

def rejectjobpost(request, id, alid):
    data=tbl_jobpost.objects.get(id=id)
    data.jobpost_status=2
    data.save()
    return redirect("Admin:viewalumnijobs", alid)

def examinationdetails(request):
    exm=tbl_examination.objects.filter(examination_status=0)
    examtype = tbl_examtype.objects.all()
    department = tbl_department.objects.all()
    if  request.method=="POST":
        name=request.POST.get("txt_name")
        qno=request.POST.get("txt_qno")
        ftime = request.POST.get("txt_ftime")
        ttime = request.POST.get("txt_ttime")

        ftime_obj = datetime.strptime(ftime, "%H:%M")
        ttime_obj = datetime.strptime(ttime, "%H:%M")
        time_diff = ttime_obj - ftime_obj
        total_seconds = time_diff.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        
        time = str(hours) +" hours and "+ str(minutes) +" minutes"
        tbl_examination.objects.create(examination_name=name,examination_mark=qno,examination_qno=qno,examination_time=time,time=str(time_diff),start_time=ftime,examtype=tbl_examtype.objects.get(id=request.POST.get("sel_examtype")),department=tbl_department.objects.get(id=request.POST.get("sel_dept")))

    return render(request,'Administrator/AddExamination.html',{'result':exm,"examtype":examtype,"department":department})

def addquestions(request, id):
    que=tbl_questions.objects.filter(examination=id)
    if  request.method=="POST":
        examination=tbl_examination.objects.get(id=id)
        questions=request.POST.get("txt_question")
        tbl_questions.objects.create(question=questions,examination=examination)
    return render(request,'Administrator/Addquestion.html',{'result':que,'id':id})

def addoptions(request, id):
    que = tbl_options.objects.filter(questions=id)
    if request.method == "POST":
        questions = tbl_questions.objects.get(id=id)
        ans = request.POST.get("txt_answer")
        status = request.POST.get("txt_radio") == "True"
        count = tbl_options.objects.filter(questions=questions, status=True).count()
        if status and count > 0:
            return render(request, 'Administrator/Addoption.html', {
                'msg': "Corrected Answer is already added",
                'result': que,
                'id': id
            })
        else:
            tbl_options.objects.create(
                answer=ans,
                questions=questions,
                status=status
            )
            return redirect("Admin:addoptions", id=id)
    else:
        return render(request, 'Administrator/Addoption.html', {'result': que, 'id': id})
    
def delexm(request,id): 
    tbl_examination.objects.get(id=id).delete()
    return redirect("Admin:examinationdetails") 

def delqus(request,id,did): 
    tbl_questions.objects.get(id=id).delete()
    return redirect("Admin:addquestions",did) 

def delopt(request,id,did): 
    tbl_options.objects.get(id=id).delete()
    return redirect("Admin:addoptions",did) 

def startexam(request, id):
    exam = tbl_examination.objects.get(id=id)
    exam.examination_status = 1
    exam.save()
    return redirect("Admin:examinationdetails")

def completedexam(request):
    exm=tbl_examination.objects.filter(examination_status__gt=0)
    return render(request,"Administrator/CompletedExam.html",{"exam":exm})

def viewresult(request, id):
    user = tbl_studentreg.objects.filter(tbl_examinationbody__examination=id)
    return render(request, "Administrator/ViewResult.html", {'user': user})

def completeexam(request, id):
    exam = tbl_examination.objects.get(id=id)
    exam.examination_status = 2
    exam.save()
    return redirect("Admin:completedexam")