from django import forms  
from .models import Blogpost  
  
class EmpForm(forms.ModelForm):  
    class Meta:  
        model = Blogpost  
        fields = "__all__"  