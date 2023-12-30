from django.shortcuts import render ,redirect
from item.models import Category, Item
from .forms import SignupForm
from django.db.models import Count, Q

 #request parameter is for reciving information about browser, ip addres, being GET or POST request, etc...

def index(request):
    items = Item.objects.filter(is_sold=False,is_deleted=False).order_by('-created_at')[0:8]
    categories = Category.objects.annotate(
    unsold_items_count = Count('items', filter=Q(items__is_sold=False, items__is_deleted=False))
    )
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