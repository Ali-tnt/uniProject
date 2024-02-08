from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border my-2'
ACTION_STYLE = 'border: 1px solid #ccc;\
        -webkit-border-radius: 5px;\
        -moz-border-radius: 5px;\
        border-radius: 10px !important;\
        padding: 2px 3px;\
        cursor: text;\
        height: 30px;\
        width: 270px;\
        cursor: pointer !important;'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'value': 0
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
                'required':'',
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
             'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'value': 0
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'is_sold': forms.CheckboxInput(attrs={
                'class': "checked:bg-blue-500 w-6 h-6 text-blue-600 border-gray-300 rounded focus:ring-transparent" 
            }),
        }

class AdminEditItemForm(forms.ModelForm):
    action_choices = (
        ('no_change', 'بدون تغییر'),
        ('is_rejected', 'عدم تایید محصول'),
        ('is_approved', 'تایید محصول'),
    )
    action = forms.ChoiceField(choices=action_choices, label='وضعیت محصول', widget=forms.Select(attrs={
                'class': "selectBox",
                'style': ACTION_STYLE
                }),)

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', 'is_sold', 'action', 'reject_msg')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
                }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
                }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
                }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES, 'value': 0
                                            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
                }),
            'is_sold': forms.CheckboxInput(attrs={
                'class': "checked:bg-blue-500 w-6 h-6 text-blue-600 border-gray-300 rounded focus:ring-transparent"
                }),
            'action': forms.Select(attrs={
                'class': "selectBox",
                'style': ACTION_STYLE
                }),
            'reject_msg': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'required':'',
                }),
        }
