# Generated by Django 4.2.7 on 2024-02-03 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_item_is_rejected_item_reject_msg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='reject_msg',
            field=models.TextField(blank=True, null=True),
        ),
    ]
