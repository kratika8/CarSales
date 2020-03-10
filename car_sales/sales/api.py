from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Cars


@csrf_exempt
def savesCars(request):
    id=request.POST.get('id','')
    type=request.POST.get('type','')
    value=request.POST.get('value','')
    c=Cars.objects.get(id=id)
    if type=="Customer_ide":
       c.Customer_id=value

    if type == "Fuel":
        c.Fuel = value

    if type == "Vehicle":
        c.VEHICLE_SEGMENT = value

    if type == "SellingPrice":
        c.SellingPrice = value

    if type == "PowerSteering":
        c.Power_steering = value

    if type == "Airbags":
        c.airbags = value

    if type == "Sunroof":
        c.sunroof = value

    if type == "MattFinish":
        c.Matt_finish = value

    if type == "MusicSystem":
        c.music_system = value

    if type == "Customer_Incomegroup":
        c.Customer_Incomegroup = value

    if type == "CustomerRegion":
        c.Customer_Region = value

    if type == "MaritalStatus":
        c.Customer_Marital_status = value



    student.save()
    return JsonResponse({"success":"Updated"})
