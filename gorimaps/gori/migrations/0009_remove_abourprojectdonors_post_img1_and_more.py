# Generated by Django 4.1.1 on 2022-10-06 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gori', '0008_abourprojectdonors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abourprojectdonors',
            name='post_img1',
        ),
        migrations.AddField(
            model_name='abourprojectdonors',
            name='post_img_first',
            field=models.ImageField(null=True, upload_to='aboutproject'),
        ),
        migrations.AddField(
            model_name='abourprojectdonors',
            name='post_img_second',
            field=models.ImageField(null=True, upload_to='aboutproject'),
        ),
    ]
