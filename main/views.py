from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406408086',
        'name': 'Maira Azma Shaliha',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)