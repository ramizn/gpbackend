from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import requests
from random import randint
# Create your views here.
#"https://sokratisii.pythonanywhere.com/getoptimal?username="+username+"&passowrd="+password+"&
# &googleUrl=" + getDirectionsUrl(mOrigin, mDestination);

#destination=31.977330, 35.842230&alternatives=true&key=AIzaSyA0DIF56VunnwkTvXDA8tB-G6UDNcvOuiA
key = "AIzaSyA0DIF56VunnwkTvXDA8tB-G6UDNcvOuiA"

def getOptimalPath(request):
    global key
    username = request.GET["username"]
    password = request.GET["password"]
    gurl = "{}&destination={}&alternatives=true&key={}".format(request.GET["googleUrl"],request.GET["destination"],key)
    response = requests.get(gurl)
    routes = response.json()["routes"]
    index = randint(0,len(routes)-1)
    #get optimal route
    return JsonResponse({"index":index,"gurl":gurl,"foundRoutes":len(routes)})

def login(request):
    return HttpResponse("login page")