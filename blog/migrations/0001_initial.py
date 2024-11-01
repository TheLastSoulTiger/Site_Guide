<<<<<<< HEAD
# Generated by Django 5.1.1 on 2024-10-16 12:44

import ckeditor.fields
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('short_description', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(default='')),
                ('expectations', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('departure_date', models.DateField(default=django.utils.timezone.now)),
                ('duration', models.IntegerField(default=1)),
                ('starting_point', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(upload_to='tours/')),
                ('organizational_details', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('available_dates', models.JSONField(blank=True, default=list)),
                ('tour_type', models.CharField(choices=[('bike', 'На вело'), ('car', 'На машине'), ('other', 'Иной странспорт'), ('walk', 'Пешком'), ('boat', 'На лодке')], default='other', max_length=10)),
                ('included_in_price', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('extra_charges', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('notes', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('review', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='blog.tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tour_images/')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_images', to='blog.tour')),
            ],
        ),
    ]
=======
# Generated by Django 5.1.1 on 2024-10-16 12:44

import ckeditor.fields
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('short_description', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(default='')),
                ('expectations', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('departure_date', models.DateField(default=django.utils.timezone.now)),
                ('duration', models.IntegerField(default=1)),
                ('starting_point', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(upload_to='tours/')),
                ('organizational_details', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('available_dates', models.JSONField(blank=True, default=list)),
                ('tour_type', models.CharField(choices=[('bike', 'На вело'), ('car', 'На машине'), ('other', 'Иной странспорт'), ('walk', 'Пешком'), ('boat', 'На лодке')], default='other', max_length=10)),
                ('included_in_price', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('extra_charges', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('notes', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('review', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='blog.tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tour_images/')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_images', to='blog.tour')),
            ],
        ),
    ]
>>>>>>> e57310cdbf4e2a766bce2e73ebfd2d90dd094d40
