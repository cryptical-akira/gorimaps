# Generated by Django 4.1.1 on 2022-10-24 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gori', '0034_postforpin_post_img_en_postforpin_post_source_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postforpin',
            name='post_img_en',
        ),
    ]
