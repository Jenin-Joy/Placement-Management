
from django.db import models
from Administrator.models import *

class tbl_jobrequest(models.Model):
    date=models.DateField(auto_now_add=True)
    status=models.IntegerField(default=0)
    jobpost=models.ForeignKey(tbl_jobpost,on_delete=models.CASCADE)
    student=models.ForeignKey(tbl_studentreg,on_delete=models.CASCADE)

class tbl_examinationbody(models.Model):
    examination = models.ForeignKey(tbl_examination, on_delete=models.CASCADE)
    student = models.ForeignKey(tbl_studentreg, on_delete=models.CASCADE)
    total_marks = models.IntegerField(default=0)
    examinationbody_status = models.IntegerField(default=0)

class tbl_examinationanswers(models.Model):
    examinationbody = models.ForeignKey(tbl_examinationbody, on_delete=models.CASCADE)
    question = models.ForeignKey(tbl_questions, on_delete=models.CASCADE)
    myanswer = models.ForeignKey(tbl_options, on_delete=models.CASCADE, related_name="myanswer", null=True)
    correct_answer = models.ForeignKey(tbl_options, on_delete=models.CASCADE,related_name="correct_answer")
    examinationanswers_statusq = models.IntegerField(default=0)

class tbl_timmer(models.Model):
    timmer = models.TimeField()
    exam = models.ForeignKey(tbl_examination, on_delete=models.CASCADE)
    timmer_status = models.IntegerField(default=0)