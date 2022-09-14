from django.shortcuts import render, redirect

from django.views import View
from django.http import JsonResponse,HttpResponseRedirect
from django.db import connection
from rest_framework.decorators import api_view
from django.http import HttpResponse
import datetime
import Infrastructure.ManageCookie
import pyodbc



@api_view(['POST', 'GET'])
def AdminPanelindex(request):
    context = {}
    template_name = "AdminPanel_Page.html"
    try:
        response = HttpResponseRedirect('/login/')
        if Infrastructure.ManageCookie.Coookie.check_session_cookie(request,"username") == 1:
            return render(request, template_name, context)
        else:
            print(Infrastructure.ManageCookie.Coookie.get_cookie(request,"username"))
            response.delete_cookie('username')
            return response

    except Exception as ex:
        return response

@api_view(['GET'])
def Logout(request):
    context = {}
    template_name = "Logout_Page.html"
    try:
        response = HttpResponseRedirect('/login/')
        response.delete_cookie('username')
        return response
    except Exception as ex:
        return render(request, template_name, context)

def page_not_found_view(request, exception):
    response = HttpResponseRedirect('/login/')
    response.delete_cookie('username')
    return response