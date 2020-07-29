"""Timetable_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from app import views
from Timetable_task import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex),
    path('register/',views.register,name="register"),
    path('create/',views.createForm,name="createform"),
    path('login/',views.login,name="login"),
    path('validate/',views.userValidation,name="loginvalidate"),
    path('timetable/',views.timeTable,name="timetable"),
    path('timetable1/',views.timeTable1,name="timetable1"),
    path('logout/',views.logout,name="logout"),
    path('savetable',views.saveTable,name="savetable")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)