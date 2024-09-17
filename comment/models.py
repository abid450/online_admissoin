from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']


    def __str__(self):
        return self.title
    
class post_M(models.Model):
    title = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)


    def __str__(self):
        return self.email