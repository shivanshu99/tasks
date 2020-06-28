from django.shortcuts import render
from .models import Blogpost,Phone,New
from django.http import HttpResponse,HttpResponseRedirect
 
from .forms import EmpForm,EmpF,Emp
  
def home(request):
    post = Blogpost.objects.all() 
    posts = New.objects.all() 
    context ={} 
    ph = list(Phone.objects.all())
    a=ph[-1]
    form = EmpForm(request.POST or None, request.FILES or None) 
    forms = Emp(request.POST or None, request.FILES or None) 
    if forms.is_valid(): 
        forms.save() 
        forms=Emp()
    if form.is_valid(): 
        form.save() 
        form=EmpForm()
    return render(request, "blog/home.html", {'form':form,'a':a,'post':post,'forms':forms,'posts':posts})


def index(request):
    thank = False
    form = EmpF(request.POST or None) 
    if form.is_valid(): 
        form.save() 
        form=EmpF()
        return HttpResponseRedirect('/blog/home/')
    return render(request, 'blog/index.html',{'form':form})



        
  
