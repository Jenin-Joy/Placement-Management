from django.contrib import admin
from django.urls import path
from User import views
app_name="User"

urlpatterns = [
    path('Homepage/',views.Homepage,name="Homepage"),
    path('Myprofile/',views.myprofile,name="myprofile"),
    path('Editprofile/',views.editprofile,name="editprofile"),
    path('Changepassword/',views.changepassword,name="changepassword"),
    path('Complaint/',views.complaint,name="complaint"),
    path("Requestjob/<int:id>",views.requestjob,name="requestjob"),
    path('Viewjobpost/',views.jobpost,name="viewjobpost"),
    path('notification/',views.notification,name="notification"),

    path('viewexam/',views.viewexam,name='viewexam'),
    path('viewquestion/<int:id>',views.viewquestion,name='viewquestion'),
    path('ajaxexamanswer/',views.ajaxexamanswer,name='ajaxexamanswer'),
    path('ajaxtimer/',views.ajaxtimer,name='ajaxtimer'),
    path('successer/',views.successer,name='successer'),

    path('viewresult/<int:id>',views.viewresult,name='viewresult'),
    path('chart/',views.chart,name='chart'),
    path('chart-data/', views.department_chart_data, name='chart_data'),
]

