from django.shortcuts import render,HttpResponse
from datetime import datetime
from .models import sensor

from django.views import View

# Create your views here.
def index(request):
    turb = sensor.objects.all()
    context={'turb':turb}
    return render(request,'pollution/index.html',context)
def graph1(request):
    turb = sensor.objects.all()
    context={'turb':turb}
    return render(request,'pollution/graph1.html',context)
def graph2(request):
    turb = sensor.objects.all()
    context={'turb':turb} 
    return render(request,'pollution/graph2.html',context)

def graph3(request):
    turb = sensor.objects.all()
    context={'turb':turb} 
    return render(request,'pollution/graph3.html',context)
def map3(request):
    return render(request,'pollution/map3.html')
def detail(request):
    return render(request,'pollution/detail.html')

def getdata(request):
    tur_value = request.GET['turbidity_value']
    water_detect=request.GET['water']
    water_flow_detect=request.GET['water_flow']
    pH=request.GET['pH']
    obj = sensor()
    obj.turbidity_value = tur_value
    obj.time=datetime.now()
    obj.water=water_detect
    obj.pH=pH
    obj.water_flow=water_flow_detect
    obj.save()
    print('Data was sent successfully')
    return HttpResponse('This is get request')
