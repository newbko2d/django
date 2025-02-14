"""
URL configuration for mkt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mkt import views

urlpatterns = [
    path('',views.index,name='home'),
    path('furniture/',views.furniture,name='furniture'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
    path('about/',views.about,name='about'),
    # path('',views.home),
    # path('admin/', admin.site.urls),
    # path('about-us/',views.about_us),
    # path('course/',views.course),
    # path('course_details/<slug:courseid>',views.coursedetails),
    # path('course_details/<courseid>',views.coursedetails),

]
