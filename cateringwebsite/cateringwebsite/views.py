from django.shortcuts import render

# def home(request):
#     return HttpResponse("Welcome to the Catering Website!")
def home(request):
    return render(request, 'homepage.html')

def services(request):
    return render(request, 'services.html')

def homie(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
