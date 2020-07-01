from django import forms
from .models import BlogUser
from django.contrib.auth import authenticate


class SignupForm(forms.ModelForm):
    password = forms.CharField(label=(u'Password'), widget=forms.widgets.PasswordInput(attrs={'class':'form-control input-sm bounceIn animation-delay2', 'placeholder': 'Passowrd', 'data-parsley-type':"email",}))
    password1 = forms.CharField(label=(u'Confirm Password'), widget=forms.widgets.PasswordInput(attrs={'class':'form-control input-sm bounceIn animation-delay2', 'placeholder': 'Confirm Password', 'data-parsley-type':"email",}))

    class Meta:
        model = BlogUser
        fields = ('first_name', 'last_name', 'phone_number', 'username', 'email', 'password', 'password1')

    def clean_password(self):
        if 'password' in self.cleaned_data and 'password1' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password1']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data['password']

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        try:
            BlogUser.objects.get(phone_number=phone_number)
            raise forms.ValidationError("Phone Number Already Exist.")
        except BlogUser.DoesNotExist:
            return self.cleaned_data['phone_number']

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    phone_number = forms.CharField(label=(u'Phone Number'), widget=forms.TextInput(attrs={'class':'form-control input-sm bounceIn animation-delay2', 'placeholder': 'Email or Phone Number', 'data-parsley-type':"email",}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password or PIN',}))

    def clean(self):
        phone_number = self.cleaned_data['phone_number']
        password = self.cleaned_data['password']
        userobject = authenticate(phone_number=phone_number, password=password)

        if userobject is not None:
            return self.cleaned_data
        else:
            raise forms.ValidationError("Phone Number and password do not match.")



