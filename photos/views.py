from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image,Location,Category
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def images(request):
    try:
        location = request.GET.get('location')
    except AttributeError:
        raise Http404()
        assert False
    if location == None:
        photos = Image.objects.all()
    else:
        photos = Image.objects.filter(location__location__icontains=location)
    categories = Category.objects.all()
    locations = Location.objects.all()
    
    return render(request, 'all-photos/photos.html',{"categories":categories,"photos":photos,"locations":locations})