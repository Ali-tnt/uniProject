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

@login_required #TODO ویو ادمینو درست کنم
def admin_dash(request):
    items = Item.objects.filter(created_by=request.user,is_deleted=False).order_by('-created_at')   
    item_waitlist = Item.objects.filter(is_deleted=False,is_approved=False).order_by('-created_at')

    return render(request, 'dashboard/admin_dash.html',{
        'items': items,
        'waitlist': item_waitlist,
        'var_class': "px-6 py-3 font-semibold text-white rounded-lg ",
    })
