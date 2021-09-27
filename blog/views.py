from blog.forms import PostCrear
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post

# Create your views here.
class HomeView(View):
    def get(self,request,*args,**kwargs):
        context = {

        }
        return render(request,'blog_list.html',context)

class CreatePostView(View):
    def get(self,request,*arg,**kwargs):
        form = PostCrear()
        context = {
            'form':form
        }
        return render(request,'blog_create_post.html',context)

    def post(self,request,*arg,**kwargs):
        if(request.method == "POST"):
            form = PostCrear(request.POST)
            if form.is_valid():
                titulo = form.cleaned_data.get('titulo')
                contenido = form.cleaned_data.get('contenido')

                p, created = Post.objects.get_or_create(titulo=titulo,contenido=contenido)
                p.save()
                return redirect('blog:home')
        context = {
            'form':form
        }
        return render(request,'blog_create_post.html',context)  


