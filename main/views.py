from django.shortcuts import render
from . models import Service


def index(request):

    # exctracting all data from database and stored in variable called services
    services = Service.objects.all()

    # category = request.GET.get('category')
    # print('category:', category)

    # categories = Category.objects.all()
    # photos = Photo.objects.all()

    context = {'services': services}

    return render(request, 'hotel.html', context)
