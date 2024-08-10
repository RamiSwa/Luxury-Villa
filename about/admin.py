from django.contrib import admin
from .models import About, FAQ, Agent, Testimonial

# Register your models here.


admin.site.register(About)
admin.site.register(FAQ)
admin.site.register(Agent)
admin.site.register(Testimonial)