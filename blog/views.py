from django.shortcuts import render

# Create your views here.

def blog(request):
    print('blog')

    context = {
        'text': 'Olá blog',
        'title': 'Página do blog'
    }

    return render(request, 'blog/index.html', context)

def exemplo(request):
    print('exemplo')

    context = {
        'text': 'Olá exemplo',
        'title': 'Página do exemplo'
    }

    return render(request, 'blog/exemplo.html', context)