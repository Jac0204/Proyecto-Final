from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from .models import Blog
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.

# Inicio - Se encarga de mostrar la siguiente pantalla después de loguearse
@login_required
def blog(request):
    blogs = Blog.objects.all()

    return render(request, 'blog.html', {
        'blogs': blogs
    })

# Crear Blog - Se encarga de insertar un blog en la base de datos
@login_required
def create_blog(request):
    if request.method == 'GET':
        return render(request, 'create_blog.html', {
            'form': BlogForm
        })
    else:
        form = BlogForm(request.POST, request.FILES)

        if not form.is_valid():
            return render(request, 'create_blog.html', {
                'form': BlogForm,
                'error': form.errors
            })
        
        try:
            new_blog = form.save(commit=False)
            new_blog.autor = request.user
            new_blog.save()

            return redirect('blog')
        except Exception as ex:
            return render(request, 'create_blog.html', {
                'form': BlogForm,
                'error': ex
            })

# Leer Blog - Se encarga de leer un blog según el id de la URL
@login_required
def read_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'read_blog.html', {
        'blog': blog
    })

# Actualizar Blog - Se encarga de actualizar el blog que le pertenece al usuario y que se seleccione
@login_required
def update_blog(request, blog_id):
    if request.method == 'GET':
        blog = get_object_or_404(Blog, pk=blog_id, autor=request.user)
        form = BlogForm(instance=blog)
        return render(request, 'update_blog.html', {
            'blog': blog,
            'form': form
        })
    else:
        blog = get_object_or_404(Blog, pk=blog_id, autor=request.user)
        form = BlogForm(request.POST, request.FILES, instance=blog)

        if not form.is_valid():
            return render(request, 'update_blog.html', {
                'blog': blog,
                'form': form,
                'error': form.errors
            })
        
        try:
            edit_blog = form.save(commit=False)
            edit_blog.fecha_edicion = datetime.now()
            edit_blog.save()
            return redirect('read_blog', blog_id=blog_id)
        except Exception as ex:
            return render(request, 'update_blog.html', {
                'blog': blog,
                'form': form,
                'error': ex
            })

# Eliminar Blog - Se encarga de eliminar de la base de datos el Blog creado por el usuario
@login_required
def delete_blog(request, blog_id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, pk=blog_id, autor=request.user)
        blog.delete()
        return redirect('blog')
    
# Acerca de Mi - Se encarga de mostrar información acerca del desarrollador
def about(request):
    return render(request, 'about.html')