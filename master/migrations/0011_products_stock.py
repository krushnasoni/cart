# Generated by Django 2.0.13 on 2019-03-25 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0010_cart_user_logs'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='stock',
            field=models.IntegerField(default=1),
        ),
    ]