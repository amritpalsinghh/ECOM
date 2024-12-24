from django.db import models

<<<<<<< HEAD
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering  = ('ordering',)
        
    def __str__(self):
        return self.title
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField()
    is_featured = models.BooleanField(default= False)
     
    
    def _str__(self):
        return self.title
    
=======
# Create your models here.
>>>>>>> e62ef8e5ce117fa5391810881def63497123de2e
