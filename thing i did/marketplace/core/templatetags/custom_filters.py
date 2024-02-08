# custom_filters.py
from django import template

register = template.Library()

@register.filter(name='default_image')
def default_image(value, default_image_path='item_images/default_image.jpg'):
    return value.url if value else default_image_path
    # return default_image_path
register.filter('default_image',default_image)