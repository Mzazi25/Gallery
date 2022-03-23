from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.location

class Category(models.Model):
    name = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.name
    @classmethod
    def search_by_category(cls,search_query):
        album = cls.objects.filter(name__icontains=search_query)
        return album

class Image(models.Model):
    Name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    photos = models.ImageField(null=False,blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    @classmethod
    def search_by_category(cls,search_term):
        news = cls.objects.filter(category=search_term)
        return news
