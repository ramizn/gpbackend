from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.
def getOptimalPath(request):
    return JsonResponse({"index":"0"})
    
