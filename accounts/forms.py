from django import forms
from .models import User


class UserForm(forms.ModelForm):
    # creating a custom field called confirm password as this field is not under general User model
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']


    def clean(self):
        # This is inbuilt method of django, here we are using it to validate the password mismatch functionality by overriding the existing clean method.
        cleaned_data = super(UserForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password!=confirm_password:
            raise forms.ValidationError(
                "Password does not match"
            )