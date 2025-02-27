# Generated by Django 5.1.5 on 2025-01-27 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('CR', 'Curd'), ('ML', 'Milk'), ('MS', 'Lassi'), ('PN', 'Milkshake'), ('GH', 'Paneer'), ('CZ', 'Ghee'), ('IC', 'Ice-Creams')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
