from django.contrib.auth.models import User
from django.db import models
from django_jalali.db import models as jmodels
from item.models import Item

class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    modified_at = jmodels.jDateTimeField(auto_now=True) 

    class Meta:
        ordering = ('-modified_at',)
    
class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='متن پیام')
    created_at = jmodels.jDateTimeField(auto_now_add=True) 
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)