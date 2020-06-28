from django import forms  
from .models import Blogpost,Phone,New
  
class EmpForm(forms.ModelForm):  
    class Meta:  
        model = Blogpost  
        fields = "__all__"  


class EmpF(forms.ModelForm):  
    class Meta:  
        model = Phone  
        fields = "__all__"  

class Emp(forms.ModelForm):  
    class Meta:  
        model = New  
        fields = "__all__" 