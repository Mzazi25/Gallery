from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40, blank=True)
    
    def __str__(self):
        return self.name
    @classmethod
    def search_by_category(cls,search_query):
        album = cls.objects.filter(name__icontains=search_query)
        return album
       
class Location(models.Model):
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.location
    
class Image(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=False,blank=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    @classmethod
    def search_by_category(cls,search_term):
        news = cls.objects.filter(category=search_term)
        return news
    
