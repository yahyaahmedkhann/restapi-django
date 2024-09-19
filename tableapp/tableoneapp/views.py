from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection

# Create your views here.
def call_stored_procedure(request):
    with connection.cursor() as cursor:
        cursor.callproc('GetAllUsers')
        results = cursor.fetchall()
        users = [{'id': row[0], 'first_name': row[1], 'last_name': row[2], 'email': row[3]} for row in results]
        return JsonResponse(users, safe=False)