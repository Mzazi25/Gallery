from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$',views.artphotos,name='newsToday'),
    re_path(r'^search/', views.search_results, name='search_results'),
    
]