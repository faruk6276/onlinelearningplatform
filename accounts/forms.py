from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label="UserName", max_length=30, required=True,
                               widget=forms.TextInput(attrs={'class': 'input_field'}))
    first_name = forms.CharField(label="First Name",max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'input_field'}))
    last_name = forms.CharField(label = "Last Name", max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'input_field'}))
    email = forms.EmailField(label = "Email",required=True, widget=forms.TextInput(attrs={'class': 'input_field'}))
    password = forms.CharField(label="Password", min_length=8,max_length=30, required=True, widget=forms.PasswordInput(attrs={'class': 'input_field'}))
    confirm_password = forms.CharField(label = "Confirm Password",min_length=8,max_length=30, required=True, widget=forms.PasswordInput(
        attrs={'class': 'input_field'}))

class LoginForm(forms.Form):
    username = forms.CharField(label="UserName", required=True,
                               widget=forms.TextInput(attrs={'class': 'input_field'}))
    password = forms.CharField(label="Password",
                               required=True, widget=forms.PasswordInput(attrs={'class': 'input_field'}))

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label="Email", required=True, widget=forms.TextInput(
        attrs={'class': 'input_field'}))
