from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Category, Item
from .forms import NewItemForm, EditItemForm


# for search an item
  # items

def browse(request): 
    query = request.POST.get('query','')
    category_id = request.POST.get('category', 0 )
    categories = Category.objects.all()
    browse = Item.objects.filter(is_sold=False,is_deleted=False,is_approved=True).order_by('-created_at')

    if category_id:
        browse = browse.filter(category_id=category_id)

    if query:
        browse= browse.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/browse.html',{
        'items' : browse,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })


# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
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
    item = get_object_or_404(Item, pk=pk, created_by=request.user or request.user==request.user.is_superuser) #TODO این شرطشو درست کنم ادمین بتونه ادیت کنه 

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save(commit=True)

            return redirect('item:detail', pk=item.id)
            
    else:
        form = EditItemForm(instance=item)


    return render(request, 'item/form.html',{
        'form' : form ,
        'title': 'ویرایش محصول',
})

# deleting an item
@login_required
def delete(request, pk):
    item = get_object_or_404(Item,pk=pk, created_by=request.user)
    item.is_deleted = True
    item.save()
    # item.delete()

    return redirect('dashboard:index')

@login_required
def sold_out(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.is_sold = not(item.is_sold)
    item.save()

    return redirect('item:detail', pk=item.id)
