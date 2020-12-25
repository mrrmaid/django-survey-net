from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import forms
from accounts.models import UserProfile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password1', 'password2', 'profile_image')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

#class LogForm(AuthenticationForm):
 #   def __init__(self, *args, **kwargs):
 #       super(LogForm, self).__init__(*args, **kwargs)

 #       self.fields['username'].widget.attrs['class'] = 'form-control'
 #       self.fields['password'].widget.attrs['class'] = 'form-control'
