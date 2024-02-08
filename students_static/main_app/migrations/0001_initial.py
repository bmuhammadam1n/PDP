# Generated by Django 4.2 on 2023-04-05 12:02

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug_name', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority_name', models.CharField(max_length=100)),
                ('priority_slug_name', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
                ('tag_slug_name', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('name_slug', models.SlugField(max_length=150)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('done', models.BooleanField(default=False)),
                ('descrition', models.TextField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categr', to='main_app.category')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='priorit', to='main_app.priority')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='main_app.tag')),
            ],
        ),
    ]