from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .models import Movie, Subscription
from django.db.models import F
from random import shuffle

def index(request):
    if request.method == 'POST':
        category = request.POST.get('category', '')
        genre = request.POST.get('genre', '')
        platform = request.POST.get('platform', '')

        if genre != '' and platform != '':
            if category == 'trending':
                movies = Movie.objects.filter(genre=genre).filter(platform=platform).order_by('-sold')
                genre_set = True
                return render(request, 'index.html', {'movies':movies, 'genre_set':genre_set})
            elif category == 'newest':
                movies = Movie.objects.filter(genre=genre).filter(platform=platform).order_by('-id')
                genre_set = True
                return render(request, 'index.html', {'movies':movies, 'genre_set':genre_set})
            elif category == 'high_to_low':
                movies = Movie.objects.filter(genre=genre).filter(platform=platform).order_by('-price')
                genre_set = True
                return render(request, 'index.html', {'movies':movies, 'genre_set':genre_set})
            elif category == 'low_to_high':
                movies = Movie.objects.filter(genre=genre).filter(platform=platform).order_by('price')
                genre_set = True
                return render(request, 'index.html', {'movies':movies, 'genre_set':genre_set})
            else:
                movies = Movie.objects.filter(genre=category).filter(platform=platform)
                genre_set = True
                return render(request, 'index.html', {'movies':movies, 'genre_set':genre_set})
        elif platform != '':
            if category == 'trending':
                movies = Movie.objects.filter(platform=platform).order_by('-sold')
                return render(request, 'index.html', {'movies':movies})
            elif category == 'newest':
                movies = Movie.objects.filter(platform=platform).order_by('-id')
                return render(request, 'index.html', {'movies':movies})
            elif category == 'high_to_low':
                movies = Movie.objects.filter(platform=platform).order_by('-price')
                return render(request, 'index.html', {'movies':movies})
            elif category == 'low_to_high':
                movies = Movie.objects.filter(platform=platform).order_by('price')
                return render(request, 'index.html', {'movies':movies})
            else:
                movies = Movie.objects.filter(platform=platform)
                return render(request, 'index.html', {'movies':movies})
        elif genre != '':
            if category == 'trending':
                movies = Movie.objects.filter(genre=genre).order_by('-sold')
                genre_set = True
                return render(request, 'index.html', {'movies':movies, 'genre_set':genre_set})
            elif category == 'newest':
                movies = Movie.objects.filter(genre=genre).order_by('-id')
                genre_set = True
                return render(request, 'index.html', {'movies':movies, 'genre_set':genre_set})
            elif category == 'high_to_low':
                movies = Movie.objects.filter(genre=genre).order_by('-price')
                genre_set = True
                return render(request, 'index.html', {'movies':movies, 'genre_set':genre_set})
            elif category == 'low_to_high':
                movies = Movie.objects.filter(genre=genre).order_by('price')
                genre_set = True
                return render(request, 'index.html', {'movies':movies, 'genre_set':genre_set})
            else:
                movies = Movie.objects.filter(genre=category)
                genre_set = True
                return render(request, 'index.html', {'movies':movies, 'genre_set':genre_set})
        else:
            if category == 'trending':
                movies = Movie.objects.all().order_by('-sold')
                return render(request, 'index.html', {'movies':movies})
            elif category == 'newest':
                movies = Movie.objects.all().order_by('-id')
                return render(request, 'index.html', {'movies':movies})
            elif category == 'high_to_low':
                movies = Movie.objects.all().order_by('-price')
                return render(request, 'index.html', {'movies':movies})
            elif category == 'low_to_high':
                movies = Movie.objects.all().order_by('price')
                return render(request, 'index.html', {'movies':movies})
            else:
                movies = Movie.objects.filter(genre=category)
                genre_set = True
                return render(request, 'index.html', {'movies':movies, 'genre_set':genre_set})

    else:
        movies = Movie.objects.all().order_by('-sold')
        genre_set = False
        return render(request, 'index.html', {'movies':movies})

def contact(request):
    return render(request, 'contact.html')

def product(request, id):
    movie = Movie.objects.get(id=id)
    productList = list(Movie.objects.filter(genre=movie.genre).exclude(id=id))
    shuffle(productList)
    
    return render(request, 'product.html', {'movie':movie, 'products': productList})

def subscribe(request):
    post_name = request.POST.get('name', False)
    post_email = request.POST.get('email', False)
    post_movie = request.POST.get('movie_id', False)
    new_item = Subscription(name = post_name, mail = post_email, movie_id = post_movie)
    new_item.save()
    messages.info(request, 'You have succesfully subscribed, we will let you know something soon!')
    return HttpResponseRedirect('/')

def addToCart(request):
    movie_id = request.POST.get('id', False)
    Movie.objects.filter(id=movie_id).update(sold=F('sold')+1)
    Movie.objects.filter(id=movie_id).update(stock=F('stock')-1)
    messages.info(request, 'Thank you for your purchase')
    return HttpResponseRedirect('/')
