from django.contrib import admin
from django.urls import path
from Guest import views
app_name="Guest"

urlpatterns = [
    path('UserRegistration/',views.UserRegistration,name="UserRegistration"),
    path('Login/',views.Login,name="Login"),
    path('',views.index,name="index"),
    path('userdashboard/',views.userdashboard,name="userdashboard"),
    path('chart-data/', views.department_chart_data, name='chart_data'),
]