from django.urls import path
from Hod import views
app_name="Hod"

urlpatterns = [
    path('myprofile/',views.myprofile,name="myprofile"),
    path('Homepage/',views.Homepage,name="Homepage"),
    path('Changepassword/',views.changepassword,name="changepassword"),
    path('Editprofile/',views.editprofile,name="editprofile"),
    path('notification/',views.notification,name="notification"),
    path('studentlist/',views.studentlist,name="studentlist"),
    path('Confirmlist/',views.confirmlist,name="confirmlist"),
    path('Placedlist/',views.placedlist,name="placedlist"),
    path('joblist/',views.viewjobs,name="Joblist"),
    path('Eligiblelist/<int:id>',views.eligiblelist,name="Eligiblelist"),

    path('viewexam/',views.viewexam,name="viewexam"),
    path('viewresult/<int:id>',views.viewresult,name="viewresult"),

    path('get_bar_chart/',views.get_bar_chart,name="get_bar_chart"),

]