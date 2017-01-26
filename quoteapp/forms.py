from django import forms
from .models import *
from django.contrib.auth import(
        authenticate,
        get_user_model,
        login,
        logout,
        )

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length = 16)
    password = forms.CharField(widget = forms.PasswordInput)
    def clean(self , *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username="username",password="password")
            if not user:
                raise forms.ValidationError("User Not Exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("User Not Active")
        return super(UserLoginForm,self).clean(*args,**kwargs)

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label="Email")
    email2 = forms.EmailField(label = "Confirm Email")
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email'
        ]
    def clean(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")
        if email!=email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email = email)
        if email_qs.exists():
            raise forms.ValidationError("Already registered")
        return super(UserRegisterForm,self).clean(*args,**kwargs)

"""
class QuotetextForm(forms.Form):
	quote = forms.CharField(max_length = 60)
	qname = forms.CharField(max_length = 20)
"""
class QuoteForm(forms.ModelForm):
    class Meta:
        model = QuoteModel
        fields =[
            'quote',
            'qname'
        ]
"""
    def clean(self,*args,**kwargs):
        quote = self.cleaned_data.get("quote")
        qname = self.cleaned_data.get("qname")
        return super(QuoteForm,self).clean(*args,**kwargs)
"""
"""
class QuoteForm(forms.ModelForm):
    quote = forms.CharField(max_length = 60)
    qname = forms.CharField(max_length = 20)
    def save(self, commit=True):
        quote = self.cleaned_data.get('quote', None)
        qname = self.cleaned_data.get('qname', None)
        # ...do something with extra_field here...
        return super(QuoteForm, self).save(commit=commit)

    class Meta:
        model = QuoteForm
        fields = "__all__"
"""
