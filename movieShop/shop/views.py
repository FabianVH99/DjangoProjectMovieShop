from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie, Subscription

def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies':movies})

def contact(request):
    return render(request, 'contact.html')

def product(request, id):
    movie = Movie.objects.get(id=id)
    products = Movie.objects.filter(genre=movie.genre).exclude(id=id)
    return render(request, 'product.html', {'movie':movie, 'products': products})

def subscribe(request):
    post_name = request.POST.get('name', False)
    post_email = request.POST.get('email', False)
    post_movie = request.POST.get('movie_id', False)
    new_item = Subscription(name = post_name, mail = post_email, movie_id = post_movie)
    new_item.save()
    return HttpResponseRedirect('/')