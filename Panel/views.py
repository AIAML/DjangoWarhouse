from django.shortcuts import render, redirect

from django.views import View
from django.http import JsonResponse
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

        return render(request, template_name, {'context': context})
    except Exception as ex:
        return render(request, template_name, context)


