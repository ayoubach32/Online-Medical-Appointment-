from django.shortcuts import render , redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm 
from .forms import CustomUserCreationForm , PatientSignupForm , AppointmentForm
from django.contrib import messages 
from django.contrib.auth import authenticate , login , logout
from .models import Appointment, Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your views here.

class Index (View):
    def get(self ,request , *args, **kwargs ):
           return render(request ,'hospital\index.html ')
    
class About (View):
    def get(self , request , *args, **kwargs):
        return render(request , 'hospital/about.html')
    
class Choose (View):
     def get(self , request , *args, **kwargs):
          return render (request , 'hospital/choose.html')
    
class Adminn (View) :
    def get(self , request , *args, **kwargs):
         return render (request , 'hospital/adminn.html')

class Patient (View) :
    def get(self , request , *args, **kwargs):
         return render (request , 'hospital/patient.html')

class Contact (View):
     def get(self , request , *args, **kwargs):
          return render(request , 'hospital/contact.html')
    

def LoginAdmin (request ):
     form = UserCreationForm()
     
     if request.method == 'POST' :
          username = username = request.POST.get('username')
          password = password = request.POST.get('password')

          user = authenticate(request , username=username , password=password)
          if user is not None :
               login(request , user)
               return redirect('adminn')
          else : 
               messages.info(request , 'Username OR password is incorrect')
     
     context= {}
     return render(request , 'hospital/loginAdmin.html' , context)
     
def login_patient(request):
     form = UserCreationForm()
     if request.method == "POST":
        username = username = request.POST.get('username')
        password = password = request.POST.get('password')
            
        client = authenticate(request ,username=username , password=password )
        if client is not None :
          login(request , client)
          return redirect('patient')
        else : 
          messages.info(request , 'Username OR password is incorrect')
      
     context= {}
     return render(request , 'hospital/loginPatient.html' , context)
     
     
def SignupAdmin(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully!'+ user)
            return redirect('adminn')  # Redirect to login page after successful signup
        else:
            messages.error(request, 'Please correct the error below.')
    else:
         form = CustomUserCreationForm()
    
    context = {'form': form}
    return render(request, 'hospital/signupAdmin.html', context)



def patient_signup(request):
    if request.method == "POST":
        form = PatientSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('patient')  # Redirect to login page after successful signup
        else:
            print(form.errors)  # Print form errors to the console
            messages.error(request, 'Please correct the error below.')
    else:
        form = PatientSignupForm()

    context = {'form': form}
    return render(request, 'hospital/signupPatient.html', context)


from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Save the form and associate the user
            appointment = form.save(commit=False)
          # Get the profile of the logged-in user
            profile = Profile.objects.get(user=request.user)
            
            # Assign the profile to the appointment
            appointment.user = profile
            
            # Save the appointment
            appointment.save()
            return redirect('appointment_success')  # Redirect to a success page or dashboard
    else:
        form = AppointmentForm()

    context = {
        'form': form,
    }
    return render(request, 'hospital/appointment.html', context)

def appointment_success(request):
    return render(request, 'hospital/appointment_success.html')


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()