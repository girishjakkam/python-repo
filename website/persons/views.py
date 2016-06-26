from django.http import HttpResponse
from django.shortcuts import render
from .models import items,subitems

def index(request):
    return render(request,'persons/index.html',{'items':items.objects.all()})

def detail(request,person_id):
   return render(request,'persons/detail.html',{'items': items.objects.get(pk=person_id)})