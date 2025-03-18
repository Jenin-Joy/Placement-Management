from django.urls import path
from Alumni import views
app_name="Alumni"

urlpatterns = [
    path('Homepage/',views.Homepage,name="Homepage"),
    path('Myprofile/',views.myprofile,name="myprofile"),
    path('Editprofile/',views.editprofile,name="editprofile"),
    path('Changepassword/',views.changepassword,name="changepassword"),
    path('Jobpost/',views.jobpost,name="jobpost"),
]