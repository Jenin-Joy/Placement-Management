from django.shortcuts import render

def calculation(request):
    if request.method=="POST":
        a=int(request.POST.get('txt_no1'))
        b=int(request.POST.get('txt_no2'))
        btn=request.POST.get('btn_submit')
        if btn=="+":
            result=a+b
        elif btn=="-":
            result=a-b
        elif btn=="*":
            result=a*b
        else:
            result=a/b
        return render(request,"Basics/Calculator.html",{'result':result})
    else:
        return render(request,'Basics/Calculator.html')
def Largest(request):
    if request.method=="POST":
        a=int(request.POST.get('txt_no1'))
        b=int(request.POST.get('txt_no2'))
        btn=request.POST.get('btn_submit')
        if a>b:
            result=a
            result1=b
        else:
            result=b
            result1=a
        return render(request,"Basics/LargestSmallest.html",{'result':result,'result1':result1})
    else:
        return render(request,'Basics/LargestSmallest.html')
