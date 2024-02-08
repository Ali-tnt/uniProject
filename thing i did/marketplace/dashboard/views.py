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
    item_waitlist = Item.objects.filter(is_deleted=False, is_approved=False).order_by('-modified_at')

    total_items_count = Item.objects.filter(is_deleted=False).count()
    total_waiting_for_sell = Item.objects.filter(is_sold=False, is_approved=True, is_deleted=False).count()
    total_waiting_for_approve = item_waitlist.count()
    total_sold_items = Item.objects.filter(is_sold=True).count()
    total_deleted_items = Item.objects.filter(is_deleted=True).count()
    stats = [
        ('تعداد کل محصولات', total_items_count),
        ('محصولات حذف شده', total_deleted_items),
        ('در انتظار تایید', total_waiting_for_approve),
        ('برای فروش', total_waiting_for_sell),
        ('محصولات فروخته شده', total_sold_items),
        
    ]
    return render(request, 'dashboard/admin_dash.html',{
        'waitlist': item_waitlist,
        'var_class': "px-6 py-3 font-semibold text-white rounded-lg ",
        'stats': stats,
    })
