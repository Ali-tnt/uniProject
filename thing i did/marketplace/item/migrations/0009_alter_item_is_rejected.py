# Generated by Django 4.2.7 on 2024-02-03 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_alter_item_reject_msg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='is_rejected',
            field=models.BooleanField(default=False, verbose_name=''),
        ),
    ]