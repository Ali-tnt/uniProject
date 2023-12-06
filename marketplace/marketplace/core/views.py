from django.shortcuts import render ,redirect
from item.models import Category, Item
from .forms import SignupForm
 #request parameter is for reciving information about browser, ip addres, being GET or POST request, etc...

def index(request):
    items = Item.objects.filter(is_sold= False)[0:6]
    categories = Category.objects.all()
    # we made the /templates/core folders and django itself findes addres that we gave in render that is those
    return render(request, 'core/index.html', {
        'categories' : categories,
        'items' : items,

    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form} )


# def logout(request):
