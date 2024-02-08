# Generated by Django 4.2.7 on 2024-02-08 12:41

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0009_alter_item_is_rejected'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='modified_at',
            field=django_jalali.db.models.jDateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='reject_msg',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات عدم تایید محصول'),
        ),
    ]