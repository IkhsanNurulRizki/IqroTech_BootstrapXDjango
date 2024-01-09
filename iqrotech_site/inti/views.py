from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'iqrotech_site/inti/inti.html')

