from django.shortcuts import render
import pyodbc
from django.views import View
from django.http import JsonResponse
from django.db import connection
from rest_framework.decorators import api_view

@api_view(['POST', 'GET'])
def index(request):
    context = {}
    template_name = "Login_Page.html"

    try:
        if request.method == 'GET':
            with connection.cursor() as cursor:
                #cursor.execute("EXECUTE @RC = [dbo].[SP_Login] @username ,@password GO")
                #data = cursor.fetchall()

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

                #return JsonResponse({ "message": "OK", "result" : "OK"}, status=200)

            return render(request, template_name, {'context': context})
    except Exception as ex:
        return render(request, template_name, context)




