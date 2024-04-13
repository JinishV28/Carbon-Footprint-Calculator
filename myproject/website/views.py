from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from django.db import connection # type: ignore
from django.views.decorators.csrf import csrf_exempt # type: ignore

@csrf_exempt
def result(request):
    print("hello")
    if request.method == 'POST':
        date = request.POST.get('date', None)
        result = request.POST.get('result', None)

        with connection.cursor() as cursor:
                # Insert data into the dataset table
                cursor.execute("INSERT INTO cfc.dataset (month, carbon_emission) VALUES (%s, %s)", [date, result])

        return HttpResponse("Data inserted successfully")
    else:
        return HttpResponse("Invalid request method")

# Create your views here.
def home(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'signin.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def predictionReport(request):
    return render(request, 'predictionReport.html')

    