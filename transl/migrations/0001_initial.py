# Generated by Django 4.1.1 on 2022-10-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CharTransl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(choices=[('image-title', 'image title'), ('image-descr', 'image description'), ('person-firstname', 'person first name'), ('person-lastname', 'person last name')], default='image-title', max_length=30)),
                ('lang', models.CharField(choices=[('en', 'English'), ('ka', 'Georgian')], default='ka', max_length=2)),
                ('val', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='MultilanguageLongText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='user_slug', max_length=40, null=True)),
                ('text_en', models.CharField(default='', max_length=512)),
                ('text_ka', models.CharField(default='', max_length=512)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MultilanguageText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_en', models.CharField(default='', max_length=64)),
                ('text_ka', models.CharField(default='', max_length=64)),
                ('slug', models.SlugField(blank=True, default='user_slug', max_length=40, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MultilanguageTextField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='user_slug', max_length=40, null=True)),
                ('text_en', models.TextField(default='')),
                ('text_ka', models.TextField(default='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
