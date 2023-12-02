# Generated by Django 4.2.7 on 2023-11-29 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=20)),
                ('total', models.IntegerField()),
                ('order', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]