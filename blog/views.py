from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.
class HomeView(View):
    def get(self,request,*args,**kwargs):
        context = {

        }
        return render(request,'blog_list.html',context)


