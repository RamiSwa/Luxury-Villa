from django.shortcuts import render
from property.models import Property, Place, Category
from django.db.models import Q, Count

# Create your views here.


def home(request):
    places = Place.objects.all().annotate(property_count=Count('property_place'))
    category = Category.objects.all()
    

    
    return render(request, 'settings/home.html', {
        'places': places ,
        'category': category,
        
    })
    
    
    
    
def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')
    

    property_list = Property.objects.filter( 
    Q(name__icontains = name) &
    Q(place__name__icontains = place)
    
    )
    
    return render(request, 'settings/home_search.html' , {'property_list': property_list} )


def category_filter(request, category):
    category = Category.objects.get(name=category)
    property_list = Property.objects.filter(category=category)


    return render(request, 'settings/home_search.html' , {'property_list': property_list} )


def contact_us(request):
    pass