from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import MyUser

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='password',widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='confirm_password',widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('user_id','password','confirm_password', 'address', 'login_fail_count')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('user_id','password','confirm_password', 'address', 'login_fail_count')

    def clean_password(self):
        return self.initial["password"]