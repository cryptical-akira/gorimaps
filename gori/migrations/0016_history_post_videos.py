# Generated by Django 4.1.1 on 2022-10-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gori', '0015_human'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='post_videos',
            field=models.FileField(null=True, upload_to='hustoryimgs', verbose_name=''),
        ),
    ]
