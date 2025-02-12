from django.http import HttpResponse
from django.shortcuts import render

def about_us(request):
    return HttpResponse("welcome to django about us page")

def course(request):
    return HttpResponse("welcome to Latest Courses")
 
def coursedetails(request,courseid):
    return HttpResponse(courseid)
 
# def home(request):
#     data= {'title':'New Home Page',
#            'body_data':'welcome to my first page check',
#            'clist':['python','java','powerbi','oracle'],
#            'Numbers':[10,20,30,40,50], 
#            'student_details':[
#                {'Name':'Niranjan','Number':'1234512345'},
#                {'Name':'abc','Number':'1234512345'}
#            ]}
#     return render(request,"index1.html",data)
 

def index(request):
    return render(request,"index.html")

def furniture(request):
    return render(request,"furniture.html")

def contact(request):
    return render(request,"contact.html")

def blog(request):
    return render(request,"blog.html")

def about(request):
    return render(request,"about.html")