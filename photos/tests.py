from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class ImageTestClass(TestCase):
    # testing image
    def setUp(self):
        self.image= Image(name = 'James', description ='image')
    # Testing  location
    def setUp(self):
        self.location= Location(location="Langata")
        # Testing  category
    def setUp(self):
        self.category= Category(category="news")
    
    # Testing Save Method
    def test_save_method(self):
        self.image.save()
        self.location.save()
        self.category.save()

    def tearDown(self):        
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

        