# Generated by Django 4.1.1 on 2022-10-24 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gori', '0032_alter_postforpin_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='postforpin',
            name='post_source',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]