from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone


# Create your views here.
def home(request):
    return render(request, 'products/home.djt')


@login_required(login_url='sign_in')
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url'] and request.POST['body'] and request.FILES['image'] and \
                request.FILES['icon']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']

            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']

            product.image = request.FILES['image']
            product.icon = request.FILES['icon']
            product.published_at = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('home')

        else:
            return render(request, 'products/create.djt', {'error': 'All fields are required'})
    else:
        return render(request, 'products/create.djt')
