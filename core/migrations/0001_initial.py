# Generated by Django 5.1.2 on 2024-10-24 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Tag Name')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Post Title')),
                ('content', models.TextField(verbose_name='Post Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='core.tag', verbose_name='Tags')),
            ],
        ),
    ]