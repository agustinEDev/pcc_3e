from django.db import models

class Blog (models.Model):
    """Un blog que el usuario puede escribir."""
    title = models.CharField(max_length = 200)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        """Devuelve una representación del modelo como cadena."""
        return self.title
    
class BlogEntry (models.Model):
    """Una entrada en un blog."""
    blog =  models.ForeignKey(Blog, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100, default = 'Sin título')
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'blog_entries'

    def __str__ (self):
        """Devuelve una representación del modelo como cadena."""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text