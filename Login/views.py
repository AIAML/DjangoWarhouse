from django.shortcuts import render
import pyodbc
from django.views import View
from django.http import JsonResponse
from django.db import connection
from rest_framework.decorators import api_view

from .forms import *
from .models import UserModel

@api_view(['POST', 'GET'])
def index(request):
    context = {}
    template_name = "Login_Page.html"
    form = RegisterModelForm(request.POST)
    try:

        with connection.cursor() as cursor:
            storedProc = "Exec [dbo].[Get_Repository_value]  @repo_title = %s"
            params = ["allvalues"]
            # Execute Stored Procedure With Parameters
            cursor.execute(storedProc, params)
            # Iterate the cursor
            row = cursor.fetchone()
            while row:
                # Print the row
                if row[0] == 1:
                    context['appname'] = row[2]
                elif row[0] == 2:
                    context['orgname'] = row[2]
                row = cursor.fetchone()
            # Close the cursor and delete it
            cursor.close()
        if request.method == 'POST' and form.is_valid():
            with connection.cursor() as cursor:
                storedProc = "Exec [dbo].[Check_Username_Password]  @username = %s,@password = %s"
                params = [form.cleaned_data['username'],form.cleaned_data['password']]
                # Execute Stored Procedure With Parameters
                cursor.execute(storedProc, params)
                # Iterate the cursor
                row = cursor.fetchone()
                while row:
                    row = cursor.fetchone()
                # Close the cursor and delete it
                cursor.close()
        return render(request, template_name, {'context': context})
    except Exception as ex:
        return render(request, template_name, context)




