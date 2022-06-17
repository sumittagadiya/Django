from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.
def index(request) :
    blog = Blogpost.objects.all()
    return render(request,'blog/index.html',{'blog':blog})

def blogpost(request,id):
    blog = Blogpost.objects.all()
    post = Blogpost.objects.filter(post_id = id)[0]
    return render(request,"blog/blogpost.html",{'total_blogs' : len(blog),'post':post})