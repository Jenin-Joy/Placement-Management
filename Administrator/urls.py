
from django.urls import path
from Administrator import views
app_name="Admin"

urlpatterns = [
    path('Adminreg/',views.adminreg,name="adminreg"),
    path('Homepage/',views.Homepage,name="Homepage"),
    path('Studentmanagement/',views.studentmanagement,name="studentmanagement"),
    path('studentreg/',views.studentreg,name="studentreg"),
    path('alumnireg/',views.alumnireg,name="alumnireg"),
    path('hod/',views.hod,name="hod"),
    path('jobpost/',views.jobpost,name="jobpost"),
    path('department/',views.department,name="department"),
    path('academicyear/',views.academicyear,name="academicyear"),
    path('examtype/',views.examtype,name="examtype"),
    path('studentlist/',views.studentlist,name="studentlist"),
    path('hodlist/',views.hodlist,name="hodlist"),
    path('viewalumni/',views.viewalumni,name="viewalumni"),
    path('viewcomplaint/',views.viewcomplaint,name="viewcomplaint"),
    path('reply/<int:id>',views.reply,name="reply"),
    path('viewalumnijobs/<int:id>',views.viewalumnijobs,name="viewalumnijobs"),
    path("deletedepartment/<int:id>",views.deletedepartment,name="deletedepartment"),
    path("editdepartment/<int:id>",views.editdepartment,name="editdepartment"),
    path("deletedacademicyear/<int:id>",views.deletedacademicyear,name="deletedacademicyear"),
    path("editacademicyear/<int:id>",views.editacademicyear,name="editacademicyear"),
    path("deletedexamtype/<int:id>",views.deletedexamtype,name="deletedexamtype"),
    path("editexamtype/<int:id>",views.editexamtype,name="editexamtype"),
    path("deletedjobpost/<int:id>",views.deletedjobpost,name="deletedjobpost"),
    path('addhod/',views.addhod,name="addhod"),
    path('addstudent/',views.addstudent,name="addstudent"),
    path('upload_excel/',views.upload_excel,name="upload_excel"),
    path('Myprofile/',views.myprofile,name="myprofile"),
    path('Changepassword/',views.changepassword,name="changepassword"),
    path('Editprofile/',views.editprofile,name="editprofile"),
    path('Notification/',views.notification,name="notification"),
    path("Deletenotification/<int:id>",views.deletenotification,name="deletenotification"),
    path('Viewjobrequest/',views.viewjobrequest,name="viewjobrequest"),
    path("deletestudent/<int:id>",views.deletestudent,name="deletestudent"),
    path('jobmanagement/',views.jobmanagement,name="jobmanagement"),
    path('Semester/',views.semester,name="semester"),
    path("deletesemester/<int:id>",views.deletesemester,name="deletesemester"),
    path("editsemester/<int:id>",views.editsemester,name="editsemester"),
    path("acceptjob/<int:id>",views.acceptjob,name="acceptjob"),
    path('Viewacceptlist/',views.acceptlist,name="acceptlist"),
    path("rejectjob/<int:id>",views.rejectjob,name="rejectjob"),
    path('Viewrejectlist/',views.rejectlist,name="rejectlist"),
    path("editstudent/<int:id>",views.editstudent,name="editstudent"),
    path('eligiblelist/<int:id>',views.eligiblelist,name="Eligiblelist"),
    path("Verifylist/<int:id>",views.verifylist,name="verifylist"),
    path("rejectjobpost/<int:id>/<int:alid>",views.rejectjobpost,name="rejectjobpost"),


    path('examinationdetails/',views.examinationdetails,name='examinationdetails'),
    path('addquestions/<int:id>',views.addquestions,name='addquestions'),
    path('addoptions/<int:id>',views.addoptions,name='addoptions'),

    path('delexm/<int:id>',views.delexm,name='delexm'),
    path('delqus/<int:id>/<int:did>',views.delqus,name='delqus'),
    path('delopt/<int:id>/<int:did>',views.delopt,name='delopt'),
    path('startexam/<int:id>',views.startexam,name='startexam'),

    path('completedexam/',views.completedexam,name="completedexam"),
    path('completeexam/<int:id>',views.completeexam,name="completeexam"),
    path('viewresult/<int:id>',views.viewresult,name="viewresult"),

    path('ajaxstudentlist/',views.ajaxstudentlist,name="ajaxstudentlist"),

]




