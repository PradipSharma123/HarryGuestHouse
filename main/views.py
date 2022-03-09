from django.shortcuts import render
from . models import Service, Category, Photo


def index(request):

    # exctracting all data from database and stored in variable called services
    services = Service.objects.all()

    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()

    context = {'services': services, 'categories':categories, 'photos':photos}

    return render(request, 'hotel.html', context)
