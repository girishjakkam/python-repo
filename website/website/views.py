from django.http import HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def login(request):
    c={}
    return render(request, 'persons/login.html',c)
def auth_view(request):
    username =request.POST.get('username','')
    password=request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')
def loggedin(request):
    return render(request,'persons/loggedin.html',{'full_name': request.user.username})
def invalid_login(request):
    return render(request,'persons/invalid_login.html')
def logout(request):
    auth.logout(request)
    return render(request,'persons/logout.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
    args = {}
    args['form']= UserCreationForm()
    return render(request,'persons/register.html',args)


def register_success(request):
    return render(request,'persons/register_success.html')