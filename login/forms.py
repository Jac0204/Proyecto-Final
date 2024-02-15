from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput
from .models import UserProfile
from django.forms import ModelForm

class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
    
    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(attrs={'class': 'form-control'})
        self.fields['password'].widget = PasswordInput(attrs={'class': 'form-control'})

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control'})

class UpdateUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'})
        }

class UpdatePasswordForm(PasswordChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(UpdatePasswordForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget = PasswordInput(attrs={'class': 'form-control'})
        self.fields['new_password1'].widget = PasswordInput(attrs={'class': 'form-control'})
        self.fields['new_password2'].widget = PasswordInput(attrs={'class': 'form-control'})

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['imagen', 'link_web']
        widgets = {
            'link_web': TextInput(attrs={'class': 'form-control'})
        }