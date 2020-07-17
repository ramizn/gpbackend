from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import requests
from random import randint
from models import Driver
from django.contrib.auth.hashers import make_password, check_password
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

'''
    email = models.EmailField(max_length=100, primary_key=True)
    password = models.CharField(max_length=500, default="")
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
    city = models.CharField(max_length=30, null=True)
    phoneNo = models.CharField(max_length=14)
    carType = models.CharField(max_length=1,default="f") #f=> fuel /e=> electrical

'''
def signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        #Check if the email already signed up
        password = request.POST["password"]
        passwordConfirmation = request.POST["password2"]
        #Check if password1 == password2
        newDriver = Driver()
        newDriver.email = email
        newDriver.password = make_password(password)
        newDriver.fName = request.POST["fname"]
        newDriver.lName = request.POST["lname"]
        newDriver.city = request.POST["city"]
        newDriver.phoneNo = request.POST["phoneNo"]
        newDriver.carType = request.POST["carType"]
        newDriver.save()
    else:
        return HttpResponse("Method not allowed")


def login(request):
    return HttpResponse("login page")