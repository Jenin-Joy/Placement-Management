from django.db import models

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)
class tbl_academicyear(models.Model):
    academicyear_name=models.CharField(max_length=50)
class tbl_department(models.Model):
    department_name=models.CharField(max_length=50)
class tbl_semester(models.Model):
    semester_name=models.CharField(max_length=50)  
class tbl_examtype(models.Model):
    examtype_name=models.CharField(max_length=50)
class tbl_hod(models.Model):
    hod_name=models.CharField(max_length=50)
    hod_email=models.CharField(max_length=50)
    hod_contact=models.CharField(max_length=50)
    department=models.ForeignKey(tbl_department,on_delete=models.CASCADE)
    hod_dob=models.DateField(null=True)
    hod_password=models.CharField(max_length=50)
class tbl_studentreg(models.Model):
    studentreg_photo=models.FileField(upload_to="Assets/User/",null=True)
    studentreg_ktuid=models.CharField(max_length=50)
    studentreg_name=models.CharField(max_length=50)
    studentreg_email=models.CharField(max_length=50)
    studentreg_contact=models.CharField(max_length=50)
    department=models.ForeignKey(tbl_department,on_delete=models.CASCADE)
    academicyear=models.ForeignKey(tbl_academicyear,on_delete=models.CASCADE)
    semester=models.ForeignKey(tbl_semester,on_delete=models.CASCADE)
    studentreg_cgpa=models.CharField(max_length=50)
    studentreg_backlog=models.CharField(max_length=50)
    studentreg_dob=models.DateField(null=True)
    studentreg_password=models.CharField(max_length=50)
class tbl_alumnireg(models.Model):
    alumnireg_name=models.CharField(max_length=50)
    alumnireg_email=models.CharField(max_length=50)
    alumnireg_contact=models.CharField(max_length=50)
    department=models.ForeignKey(tbl_department,on_delete=models.CASCADE)
    academicyear=models.ForeignKey(tbl_academicyear,on_delete=models.CASCADE)
    alumnireg_dob=models.DateField(null=True)
    alumnireg_password=models.CharField(max_length=50)
class tbl_jobpost(models.Model):
    jobpost_details=models.CharField(max_length=50)
    jobpost_companyname=models.CharField(max_length=50)
    jobpost_mincgpa=models.CharField(max_length=50)
    department=models.ForeignKey(tbl_department,on_delete=models.CASCADE)
    jobpost_backlog=models.CharField(max_length=50)
    jobpost_file_doc=models.CharField(max_length=50)
    jobpost_lastdate=models.DateField()
    alumini=models.ForeignKey(tbl_alumnireg,on_delete=models.CASCADE,null=True)
    jobpost_status = models.IntegerField(default=0)
class tbl_complaint(models.Model):
    complaint_content=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=50)
    status=models.IntegerField(default=0)
    student=models.ForeignKey(tbl_studentreg,on_delete=models.CASCADE)

class tbl_examination(models.Model):
    examination_name=models.CharField(max_length=50) 
    examination_mark=models.CharField(max_length=50) 
    examination_qno=models.CharField(max_length=50) 
    examination_time=models.CharField(max_length=50) 
    examination_status = models.IntegerField(default=0)
    examination_date = models.DateField(null=True)
    time = models.TimeField(null=True)
    start_time = models.TimeField(null=True)
    examtype = models.ForeignKey(tbl_examtype, on_delete=models.CASCADE)
    department = models.ForeignKey(tbl_department, on_delete=models.CASCADE)

class tbl_questions(models.Model):
    question=models.CharField(max_length=100) 
    examination=models.ForeignKey(tbl_examination,on_delete=models.CASCADE)

class tbl_options(models.Model):
    questions=models.ForeignKey(tbl_questions,on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)
    status = models.BooleanField() 


class tbl_notification(models.Model):
    notification_notification=models.CharField(max_length=50)
    notification_limit=models.CharField(max_length=50)



