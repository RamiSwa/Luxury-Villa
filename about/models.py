from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# our agents = name + role + image user
# testimonials = image + description + name user + role user


class About(models.Model):
    what_we_do = models.TextField(max_length=1000) # Our Story
    our_mission = models.TextField(max_length=1000)  #Our Vision 
    our_goals = models.TextField(max_length=1000) 
    image = models.ImageField(upload_to='about/')  
    

    
    def __str__(self):
        return str(self.id) 
    
    
class FAQ(models.Model):
    title = models.CharField(max_length=150)  
    description = models.TextField(max_length=3000)

    def __str__(self):
        return self.title 


class Agent(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='agents/')
    fb_link = models.URLField(max_length=200)
    tw_link = models.URLField(max_length=200)
    ins_link = models.URLField(max_length=200)

    def __str__(self):
        return self.name   


class Testimonial(models.Model):
    author = models.ForeignKey(User, related_name='user_testimonial', on_delete=models.CASCADE)
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='testimonials/')
    description = models.TextField(max_length=300)
    role = models.CharField(max_length=100)
    
    

    def __str__(self):
        return self.author    
    