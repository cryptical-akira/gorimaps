# Generated by Django 4.1.1 on 2022-10-26 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gori', '0037_postforpin_post_source_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='postforpin',
            name='post_location',
            field=models.TextField(blank=True, default='', max_length=500, null=True),
        ),
    ]
