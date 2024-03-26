from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect

from .models import Blog, BlogEntry
from .forms import BlogForm, BlogEntryForm

def index(request):
    """La página de iniicio de la aplicación de blogs."""
    entries = []
    blogs = Blog.objects.order_by('date_added')
    for blog in blogs:
        entries += blog.blogentry_set.order_by('-date_added')[:5]
    context = {'blogs': blogs, 'entries': entries}
    return render(request, 'blogs/index.html', context)

@login_required
def blogs(request):
    """Muestra todos los blogs."""
    blogs = Blog.objects.filter(owner = request.user).order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

@login_required
def blog(request, blog_id):
    """Muestra un blog concreto y todas sus entradas."""
    blog = Blog.objects.get(id = blog_id)

    entries = blog.blogentry_set.order_by('-date_added')
    context = {'blog': blog, 'entries': entries}
    return render(request, 'blogs/blog.html', context)

@login_required
def new_blog(request):
    """Añade un blog nuevo."""
    if request.method != 'POST':
        # No se ha enviado datos; se crea un formulario en blanco.
        form = BlogForm()
    else:
        # Datos POST enviados; procesa datos.
        form = BlogForm(data = request.POST)
        if form.is_valid():
            new_blog = form.save(commit = False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:blogs')
        
    # Muestra un formulario en blanco o inválido.
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def new_entry(request, blog_id):
    """Añade una entrada nueva para un blog en particular."""
    blog = Blog.objects.get(id = blog_id)
    # Comprueba si el usuario actual es el propietario del blog.
    response = check_blog_owner(request, blog_id)
    if response == 'error':
        return redirect('blogs:error')

    if request.method != 'POST':
        # No se ha enviado datos; se crea un formulario en blanco.
        form = BlogEntryForm()
    else:
        # Datos POST enviados; procesa los datos.
        form = BlogEntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.blog = blog
            new_entry.save()
            return redirect('blogs:blog', blog_id = blog_id)
        
    # Muestra un formulario en blanco o inválido.
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edita una entrada existente."""
    entry = BlogEntry.objects.get(id = entry_id)
    blog = entry.blog

    # Comprueba si el usuario actual es el propietario del blog.
    response = check_blog_owner(request, blog.id)
    if response == 'error':
        return redirect('blogs:error')

    if request.method != 'POST':
        # Se rellena el formulario con la entrada actual.
        form = BlogEntryForm(instance = entry)
    else:
        # Datos POST enviados; procesa los datos.
        form = BlogEntryForm(instance = entry, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id = blog.id)
    
    context = {'entry': entry, 'blog': blog, 'form': form}
    return render(request, 'blogs/edit_entry.html', context)

def check_blog_owner(request, blog_id):
    """Comprueba si el usuario actual es el propietario del blog."""
    blog = Blog.objects.get(id = blog_id)
    if blog.owner != request.user:
        return 'error'
    else:
        return blog

def error(request):
    """Página de error cuando intentan editar o crear en un blog que no es suyo."""
    return render(request, 'blogs/error.html')