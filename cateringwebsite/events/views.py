from django.shortcuts import render
from .models import MenuItem
from .forms import ContactForm

# Create your views here.
def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'events/menu.html', {'menu_items': items})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    return render(request, 'events/contact.html', {'form': form})