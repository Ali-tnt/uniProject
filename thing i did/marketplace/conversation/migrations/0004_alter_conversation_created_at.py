# Generated by Django 4.2.7 on 2024-01-11 19:04

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0003_alter_conversation_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='created_at',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
    ]
