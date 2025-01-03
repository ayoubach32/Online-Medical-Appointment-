from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms
from .models import Profile , Doctor , Appointment

#Admin registration from ##########
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    

##Patient registration form ###################

class PatientSignupForm(UserCreationForm):
        email = forms.EmailField(required=True)
        first_name = forms.CharField(max_length=30)
        last_name = forms.CharField(max_length=30)
        address = forms.CharField(max_length=100)
        city = forms.CharField(max_length=50)
        date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1950, 2025)))
     

        class Meta:
            model = User
            fields = [ "username", "email", "password1", "password2", "first_name", "last_name", "address", "city", "date_of_birth"]
            
        def save(self, commit=True):
            user = super().save(commit=False)
            user.username = self.cleaned_data["username"]
            if commit:

                user.save()
                profile , created = Profile.objects.get_or_create(
                user=user,
                defaults={
                 'email' : self.cleaned_data['email'],
                 'first_name':self.cleaned_data["first_name"],
                 'last_name':self.cleaned_data["last_name"],
                 'address':self.cleaned_data["address"],
                 'city':self.cleaned_data["city"],
                 'date_of_birth':self.cleaned_data["date_of_birth"],
                }
                
            )
            return user


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time']
        widgets = {
            'date': forms.SelectDateWidget,
            'time': forms.TimeInput(attrs={'type': 'time'})
        }