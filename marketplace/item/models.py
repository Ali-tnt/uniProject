from django.contrib.auth.models import User
from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category , related_name='items',on_delete=models.CASCADE,verbose_name='دسته بندی')
    name = models.CharField(max_length=255,verbose_name='نام محصول')
    description = models.TextField(blank=True, null=True,verbose_name='توضیحات')
    price = models.FloatField(verbose_name='قیمت')
    image = models.ImageField(upload_to='item_images',blank=True,null=True,verbose_name='عکس محصول')
    is_sold = models.BooleanField(default=False,verbose_name='آیا محصول فروخته شده است؟')
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False,verbose_name='آیا محصول مورد تایید است؟')
    is_rejected = models.BooleanField(default=False,)
    reject_msg = models.TextField(blank=True, null=True, verbose_name='توضیحات عدم تایید محصول')
    modified_at = jmodels.jDateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    