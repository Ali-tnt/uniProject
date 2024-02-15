from django.shortcuts import render ,redirect
from item.models import Category, Item
from .forms import SignupForm
from django.db.models import Count, Q
from django.contrib import messages
from django.contrib.auth import logout

 #request parameter is for reciving information about browser, ip addres, being GET or POST request, etc...
def index(request):
    items = Item.objects.filter(is_sold=False, is_deleted=False, is_approved=True).order_by('-modified_at')[0:8]
    categories = Category.objects.annotate(
        unsold_items_count=Count('items', filter=Q(items__is_sold=False, items__is_deleted=False, items__is_approved=True))
    )

    # Check if the user has just logged in
    if request.user.is_authenticated and not request.session.get('logged_in', False):
        messages.success(request, 'با موفقیت به حساب خود وارد شدید.')
        request.session['logged_in'] = True

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
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

def custom_logout(request):
    logout(request)
    messages.success(request, 'با موفقیت از حساب خود خارج شدید.')
    return redirect('/login/') 