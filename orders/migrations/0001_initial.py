# Generated by Django 3.2.4 on 2021-08-26 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0004_auto_20210622_0604'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_foods', models.PositiveSmallIntegerField(default=0)),
                ('final_price', models.PositiveIntegerField(verbose_name='финальная сумма')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=16, verbose_name='номер телефона')),
                ('address', models.CharField(max_length=255, verbose_name='адрес')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='CartFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='количество')),
                ('total_price', models.PositiveIntegerField(verbose_name='общая сумма')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_foods', to='orders.cart', verbose_name='корзина')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.food', verbose_name='блюдо')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.customer', verbose_name='покупатель')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='foods',
            field=models.ManyToManyField(blank=True, related_name='foods_cart', to='orders.CartFood'),
        ),
        migrations.AddField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.customer', verbose_name='покупатель'),
        ),
    ]
