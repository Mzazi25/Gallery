from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image,Location,Category
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def artphotos(request):
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

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_category = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"category": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})
def photo(request,photo_id):
    try:
        photo = Image.objects.get(id = photo_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-photos/singlePhoto.html", {"photo":photo})