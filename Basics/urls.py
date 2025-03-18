
from django.contrib import admin
from django.urls import path
from Basics import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Calculator/',views.calculation,name="calculation"),
    path('LargestSmallest/',views.Largest,name="Largest"),
]   