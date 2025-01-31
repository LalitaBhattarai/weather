from django.shortcuts import render
import requests
from django.contrib import messages
# Create your views here.

def index(request):
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city="kathmandu"

    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6d3e287c97dae892c2531736150c1276"
    parameter={'units': 'metric'}


    try:
        data=requests.get(url,parameter).json()
        temp=data['main']['temp']
        desc=data['weather'][0]['description']
        icon=data['weather'][0]['icon']
        humidity=data['main']['humidity']
        wind_speed = data['wind']['speed']


        
        return render(request,"index.html",{'temp':temp,'city':city,'desc':desc,'icon':icon,'humidity':humidity,'wind_speed':wind_speed})
    
    except:
        data=requests.get(url,parameter).json()
        temp=0
        desc="there is no such city"
        messages.error(request,"City unavailable")
        return render(request,"index.html",{'temp':temp,'city':city,'desc':desc,})

       

