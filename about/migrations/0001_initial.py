# Generated by Django 5.1 on 2024-08-09 21:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_we_do', models.TextField(max_length=1000)),
                ('our_mission', models.TextField(max_length=1000)),
                ('our_goals', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='about/')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='agents/')),
                ('fb_link', models.URLField()),
                ('tw_link', models.URLField()),
                ('ins_link', models.URLField()),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.about')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='testimonials/')),
                ('description', models.TextField(max_length=300)),
                ('role', models.CharField(max_length=100)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.about')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_testimonial', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
