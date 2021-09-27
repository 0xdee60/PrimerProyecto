import django
from blog.forms import PostCrear
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class HomeView(View):
    def get(self,request,*args,**kwargs):
        posts = Post.objects.all()
        context = {
            'posts':posts
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

class PostDetailsView(View):
    def get(self,request,pk,*args, **kwargs):
        post = get_object_or_404(Post,pk=pk)
        context = {
            'post':post
        }
        return render(request,'blog_post_details.html',context)


class PostUpdateView(UpdateView):
    model = Post
    fields = ['titulo','contenido']
    template_name = 'blog_post_update.html'
    def get_success_url(self,):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:details',kwargs={'pk':pk})

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog_post_delete.html'
    success_url = reverse_lazy('blog:home')
    