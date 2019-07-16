from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.views.generic import View


class LoginView(View):
    def get(self,request):
        return render(request,"gift/login.html")

class RegistView(View):
    def get(self,request):
        return render(request,"gift/login.html")










