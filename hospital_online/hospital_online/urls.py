"""
URL configuration for hospital_online project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path , include
from hospital.views import Index , About  , Adminn , Patient , Choose , Contact 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('hospital.urls') ),
    path('', Index.as_view() , name='index'),
    path('about/' , About.as_view() , name ='about'),
    path('choose/' , Choose.as_view() , name = 'choose'),
    path('adminn/', Adminn.as_view() , name='adminn'),
    path('patient/', Patient.as_view() , name= 'patient'),
    path('contact/' , Contact.as_view() , name = 'contact'),
    #path('appointment/' , Appointment.as_view() , name='appointment')
    
   
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
