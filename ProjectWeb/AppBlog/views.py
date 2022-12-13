from django.shortcuts import render
from AppBlog.models import Categoria, Post


# Create your views here.
def blog (request):
    posts = Post.objects.all()
    return render (request , 'AppBlog/blog.html' , {'posts' : posts})

def categoria (request , categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)  
    posts = Post.objects.filter(categoria=categoria)
    return render (request, 'AppBlog/categoria.html' , {'categoria' : categoria , 'posts' : posts})