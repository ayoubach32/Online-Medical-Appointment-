from . import views 
from django.urls import path


urlpatterns = [
    path('signup/' , views.SignupAdmin , name = 'signupAdmin'),
    path('login/' , views.LoginAdmin , name = 'loginAdmin'),
    path ('signupP/' , views.patient_signup , name = 'signupPatient'),
    path ('loginP/' , views.login_patient , name = 'login_patient'),
    path('appointment/' , views.appointment , name= 'appointment'),
    path('appointment_succes/' , views.appointment_success , name= 'appointment_success'),
    
 
]



