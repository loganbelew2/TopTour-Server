# Generated by Django 4.2.5 on 2023-09-11 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('coordinates', models.CharField(max_length=255)),
                ('icon_url', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
                ('total_ratings', models.IntegerField()),
                ('photo_url', models.CharField(max_length=255)),
                ('price_level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=50)),
                ('profile_image', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toptourapi.attraction')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toptourapi.category')),
                ('tourist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toptourapi.tourist')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toptourapi.post')),
                ('tourist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toptourapi.tourist')),
            ],
        ),
    ]
