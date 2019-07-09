from django import forms
from .models import VoteUser


# 登录表单类
class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=20,required=True,widget=forms.TextInput(attrs={"id":"username","class":"form-control","placeholder":"输入用户名"} ))
    password = forms.CharField(max_length=20,required=True,widget=forms.PasswordInput(attrs={"class":"form-control", "id":"password", "placeholder":"输入密码",})  )

# 注册表单类
class RegistForm(forms.ModelForm):
    repeatpassword = forms.CharField(label="重复密码",required=True,widget=forms.PasswordInput(attrs={"class":"form-control","id":"registpassword2", "placeholder":"输入确认密码"}))
    class Meta:
        model = VoteUser
        fields = ["username","password","phone",]
        widgets = {
            "username":forms.TextInput(attrs={"id":"registusername","placeholder":"输入用户名","class":"form-control" }),
            "password":forms.PasswordInput(attrs={"class":"form-control","id":"registpassword", "placeholder":"输入密码"}),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "id": "phone", "placeholder": "输入手机号"}),
        }
        help_texts = {
            "username":"",
        }
        labels = {
            "phone":"手机号"
        }