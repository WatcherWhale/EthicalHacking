from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args,**kwargs)
        self.fields['username'].label = "Username"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm password"

class AuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthForm, self).__init__(*args,**kwargs)
        self.fields['username'].label = "Username"
        self.fields['password'].label = "Password"
