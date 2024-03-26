"""Define patrones de URL para Blogs."""

from django.urls import path

from . import views
app_name = 'blogs'
urlpatterns = [
    # Página de inicio
    path('', views.index, name = 'index'),
    # Página que muestra todos los blogs
    path('blogs/', views.blogs, name = 'blogs'),
    # Página de detalles para un blog individual
    path('blogs/<int:blog_id>/', views.blog, name = 'blog'),
    # Página para añadir un blog nuevo
    path('new_blog/', views.new_blog, name = 'new_blog'),
    # Página para añadir una nueva entrada
    path('new_entry/<int:blog_id>/', views.new_entry, name = 'new_entry'),
    # Página para editar una entrada
    path('edit_entry/<int:entry_id>/', views.edit_entry, name = 'edit_entry'),
    # Página de error cuando intentan editar o crear en un blog que no es suyo
    path('error/', views.error, name = 'error'),
]