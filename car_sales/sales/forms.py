from django import forms 
from .models import Cars 
  
  
# creating a form 
class CarsForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = Cars 
  
        # specify fields to be used 
        fields = [ 
        	"sales_id",
            "pub_date", 
            "Customer_id", 
            "Fuel", 
            "VEHICLE_SEGMENT", 
            "SellingPrice",
            "Power_steering", 
            "airbags", 
            "sunroof", 
            "Matt_finish", 
            "music_system", 
            "Customer_Gender", 
            "Customer_Incomegroup", 
            "Customer_Region", 
            "Customer_Marital_status"
            ] 