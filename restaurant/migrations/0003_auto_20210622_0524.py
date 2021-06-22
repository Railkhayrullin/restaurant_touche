# Generated by Django 3.2.4 on 2021-06-22 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20210321_1552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurantimage',
            options={'verbose_name': 'Фото ресторана', 'verbose_name_plural': 'Фото ресторана'},
        ),
        migrations.AlterField(
            model_name='restaurantimage',
            name='image',
            field=models.ImageField(upload_to='restaurant_image/', verbose_name='Фото ресторана'),
        ),
    ]
