# Generated by Django 2.0.13 on 2019-03-05 09:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecom', '0005_auto_20190305_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.TextField()),
                ('price', models.FloatField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.Users')),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Category')),
            ],
        ),
    ]
