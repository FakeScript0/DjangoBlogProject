from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "Kullanıcı Adı")
    password = forms.CharField(label = "Parola",widget = forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50,label = "Istifadeci Adi")
    password = forms.CharField(max_length=20,label = "Sifre",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label ="Sifreyi Dogrula",widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Sifre Uyusmur")

        values = {
            "username" : username,
            "password" : password
        }
        return values


