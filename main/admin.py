from django.contrib import admin
from . models import Service

# register the model in the admin section to manage
# admin object which has attribute called site which is itself
# a object and this object has method called register
# we call this method and passing model class as a argument

admin.site.register(Service)  # service = argument / register = method
# admin.site.register(Category)
# admin.site.register(Photo)
