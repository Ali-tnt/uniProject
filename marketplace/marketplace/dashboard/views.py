from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from item.models import Item

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user,is_deleted=False).order_by('-created_at')   

    return render(request, 'dashboard/index.html',{
        'items': items,
        'var_class': "px-6 py-3 font-semibold text-white rounded-lg ",
    })
