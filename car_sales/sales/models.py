from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



class Cars(models.Model):
    CHOICES = [('1', '1'), ('0', '0')]
    GCHOICES = [('Male', 'Male'), ('Female', 'Female')]
    sales_id = models.IntegerField(primary_key=True)
    pub_date = models.DateField(null=True)
    Customer_id = models.IntegerField(null=True, blank=True, default=None)
    Fuel = models.CharField(max_length=50)
    VEHICLE_SEGMENT = models.CharField(max_length=50)
    SellingPrice = models.IntegerField(null=True, validators=[MaxValueValidator(1000000)])
    Power_steering = models.CharField( max_length=5, choices=CHOICES)
    airbags = models.CharField(max_length=5, choices=CHOICES)
    sunroof = models.CharField(max_length=5, choices=CHOICES)
    Matt_finish = models.CharField(max_length=5, choices=CHOICES)
    music_system = models.CharField(max_length=5, choices=CHOICES)
    Customer_Gender = models.CharField(max_length=10, choices=GCHOICES)
    Customer_Incomegroup = models.CharField(max_length=200, null=False)
    Customer_Region = models.CharField(max_length=200)
    Customer_Marital_status = models.CharField(max_length=5, choices=CHOICES)

    def __str__(self):
        return f'{self.sales_id}'


