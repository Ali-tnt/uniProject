from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Max
from .models import Category, Item
from .forms import NewItemForm, EditItemForm, AdminEditItemForm
from django.http import Http404

# from django.contrib import messages

# for search an item
  # items
def browse(request):
    categories = Category.objects.all()
    browse_items = Item.objects.filter(is_sold=False, is_deleted=False, is_approved=True).order_by('-modified_at')
    custom_value = 10000
    highest_item_price = custom_value + Item.objects.filter(is_sold=False, is_deleted=False, is_approved=True).aggregate(Max('price'))['price__max'] or 0 

    if request.method == 'POST':
        query = request.POST.get('query', '')
        category_id = request.POST.get('category', 0) or 0
        min_price = request.POST.get('min_price')
        max_price = request.POST.get('max_price')
        order = request.POST.get('order', 'newest')

        if category_id:
            browse_items = browse_items.filter(category_id=int(category_id))
        else:
            category_id = 0

        if query:
            browse_items = browse_items.filter(Q(name__icontains=query) | Q(description__icontains=query))

        if min_price:
            min_price = float(min_price)
            browse_items = browse_items.filter(price__gte=min_price)
        if max_price:
            max_price = float(max_price)
            browse_items = browse_items.filter(price__lte=max_price)

        if order == 'newest':
            browse_items = browse_items.order_by('-modified_at')
        elif order == 'oldest':
            browse_items = browse_items.order_by('modified_at')
        elif order == 'high_to_low':
            browse_items = browse_items.order_by('-price')
        elif order == 'low_to_high':
            browse_items = browse_items.order_by('price')

    else:
        query = ""
        category_id = 0
        min_price = 0
        max_price = highest_item_price
        order = 'newest'  # Default order

    return render(request, 'item/browse.html', {
        'items': browse_items,  
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
        'min_price': min_price,
        'max_price': max_price,
        'highest_item_price': highest_item_price,
        'price_order': order  # Passing order for highlighting selected link
    })


# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if not (request.user.is_superuser or item.created_by == request.user) and item.is_rejected:
        raise Http404("چنین محصولی وجود ندارد")

    related_items = Item.objects.filter(category=item.category, is_sold=False, is_deleted=False,is_approved=True).exclude(pk=pk)[0:3] 
    
    return render(request, 'item/detail.html', {
        'item': item, 
        'related_items': related_items 
    })
# adding an item
@login_required
def new_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html',{
        'form' : form ,
        'title': 'ثبت محصول',
})
# editing an item
@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if not (request.user == item.created_by or request.user.is_superuser):
        return render(request, 'core/403.html', status=403)

    if request.method == 'POST':
        if request.user.is_superuser:
            form = AdminEditItemForm(request.POST, request.FILES, instance=item)
        else:
            form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            if request.user.is_superuser:
                action = form.cleaned_data.get('action')  # Use get() method to avoid KeyError
                if action == 'is_rejected':
                    item.is_rejected = True
                    item.is_approved = False
                elif action == 'is_approved':
                    item.is_rejected = False
                    item.is_approved = True
            else: # if user edited, item would go to admin check state
                item.is_approved = False
                item.is_rejected = False
            form.save()
            return redirect('item:detail', pk=item.id)
    else:
        if request.user.is_superuser:
            form = AdminEditItemForm(instance=item)
        else:
            form = EditItemForm(instance=item)
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'ویرایش محصول',
        'user': request.user,
    })

# deleting an item
@login_required
def delete(request, pk):
    item = get_object_or_404(Item,pk=pk)

    if (item.created_by == request.user or request.user.is_superuser):
        item.is_deleted = True
        item.save()
        # item.delete()
    else:
        return render(request, 'core/403.html', status=403)
    
    return redirect('dashboard:index')

@login_required
def sold_out(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if (item.created_by == request.user or request.user.is_superuser):
        item.is_sold = not(item.is_sold)
        item.save()
    else:
        return render(request, 'core/403.html', status=403)

    return redirect('item:detail', pk=item.id)
