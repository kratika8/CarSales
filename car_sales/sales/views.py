import csv, io
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cars
from django.http import HttpResponse
from django.db.models import Q
import pandas as pd
import os
from .forms import CarsForm
from django.http import HttpResponseRedirect



def index(request):
    return render(request, 'home.html')

def car_upload(request):
    template = "cars.html"
    prompt = {
        'order': ' '
    }
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']
    dfs = pd.read_csv(csv_file)
    dfs = pd.DataFrame(dfs)
    dfs['Date of Purchase'] = pd.to_datetime(dfs['Date of Purchase'] )
    dfs['Date of Purchase'] = dfs['Date of Purchase'].dt.date
    for i in range(len(dfs)) :    
        Cars.objects.update_or_create(
        sales_id= dfs.iloc[i, 0],
        pub_date= dfs.iloc[i, 1],
        Customer_id=dfs.iloc[i, 2],
        Fuel=dfs.iloc[i, 3],
        VEHICLE_SEGMENT=dfs.iloc[i, 4],
        SellingPrice=dfs.iloc[i, 5],
        Power_steering=dfs.iloc[i, 6],
        airbags= dfs.iloc[i, 7],
        sunroof=dfs.iloc[i, 8],
        Matt_finish= dfs.iloc[i, 9],
        music_system= dfs.iloc[i, 10],
        Customer_Gender=dfs.iloc[i, 11],
        Customer_Incomegroup=dfs.iloc[i, 12],
        Customer_Region=dfs.iloc[i, 13],
        Customer_Marital_status=dfs.iloc[i, 14],
        )

    context = {}
    return render(request, template, context)

def fetch(request):
    all_cars = Cars.objects.all()
    return render(request, "index.html", {'ListCars':all_cars}) 


def searchposts(request):
    if request.method == 'POST':

        srch = request.POST['srh']
        if srch:
            match = Cars.objects.filter(Q(sales_id__icontains=srch) | Q(Customer_id__icontains=srch))

            if match:
                return render(request, "search.html", {'sr': match})
            else:
                messages.error(request, 'no result found')
        else:
            return HttpResponseRedirect('/seachdata/')

    return render(request, 'search.html')


def addData(request):
    return render(request, 'add.html')

def submitadd(request):
    sales_id = request.POST['sales_id']
    pub_date = request.POST['pub_date']
    Customer_id = request.POST['Customer_id']
    Fuel = request.POST['Fuel']
    VEHICLE_SEGMENT = request.POST['VEHICLE_SEGMENT']
    SellingPrice = request.POST['SellingPrice']
    Power_steering = request.POST['Power_steering']
    airbags = request.POST['airbags']
    sunroof = request.POST['sunroof']
    Matt_finish = request.POST['Matt_finish']
    music_system = request.POST['music_system']
    Customer_Gender = request.POST['Customer_Gender']
    Customer_Incomegroup = request.POST['Customer_Incomegroup']
    Customer_Region = request.POST['Customer_Region']
    Customer_Marital_status = request.POST['Customer_Marital_status']

    data_put = Cars(sales_id=sales_id, pub_date=pub_date, Customer_id=Customer_id, Fuel=Fuel, VEHICLE_SEGMENT=VEHICLE_SEGMENT, SellingPrice=SellingPrice, Power_steering=Power_steering, airbags=airbags, sunroof=sunroof, Matt_finish=Matt_finish, music_system=music_system, Customer_Gender=Customer_Gender, Customer_Incomegroup=Customer_Incomegroup, Customer_Region=Customer_Region, Customer_Marital_status=Customer_Marital_status)
    
    data_put.save()
    return render(request, 'add.html')

# def update_view(request, sales_id):
#     obj = get_object_or_404(Cars, sales_id=sales_id)
#     form = CarsForm(request.POST or None, instance = obj)
#     if form.is_valid():
#         form.save()  
#         return redirect(sales_id+'/update_view/') 
#     else:
#         form = CarsForm(instance=obj)
#     context = {'form' : form } 
#     return render(request, "update_view.html", context)