from django.shortcuts import render
from property.models import Property, Place, Category
from .models import Settings
from django.db.models import Q, Count
from django.core.mail import send_mail
from django.conf import settings
from .tasks import send_mail_task
from django.contrib.auth.models import User
from property import models as property_models
from blog import models as blog_models

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
    site_info = Settings.objects.last()

    if request.method == 'POST':
        subject = request.POST['subject']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']


        send_mail_task.delay(subject , name,email,message)


    return render(request,'settings/contact.html',{'site_info': Settings})



def dashboard(request):
    users_count = User.objects.all().count()
    apartments_count = property_models.Property.objects.filter(category__name='Apartment').count()
    villa_count = property_models.Property.objects.filter(category__name='Villa').count()
    suits_count = property_models.Property.objects.filter(category__name='suite').count()
    posts = blog_models.Post.objects.all().count()
    booking = property_models.PropertyBook.objects.all().count()
    
    return render(request, 'settings/dashboard.html', {
        'users_count' : users_count , 
        'apartments_count': apartments_count , 
        'villa_count' : villa_count  , 
        'suits_count' : suits_count ,  
        'posts_count' : posts , 
        'booking_count' : booking
    })