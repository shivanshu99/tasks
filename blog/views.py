from django.shortcuts import render
from .models import Blogpost,Message

from django.http import HttpResponse,HttpResponseRedirect
 
from .forms import EmpForm  
  
def home(request): 
    context ={} 
  
    form = EmpForm(request.POST or None, request.FILES or None) 

    if form.is_valid(): 

        form.save() 
        return HttpResponseRedirect('/blog/')
  
    context['form']= form 
    return render(request, "blog/home.html", context)


def index(request):
    myposts = Blogpost.objects.all()

    return render(request, 'blog/index.html',
                  {'myposts': myposts})

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    posts = Message.objects.all()
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        commentId=request.POST.get('commentId','')
        desc = request.POST.get('desc', '')
        blogpost = Message(name=name,  desc=desc,commentId=commentId)
        blogpost.save()
        thank = True
       
    return render(request, 'blog/blogpost.html',
                  {'post':post,'posts':posts})


    
        
  
