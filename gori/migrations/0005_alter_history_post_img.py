# Generated by Django 4.1.1 on 2022-10-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gori', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='post_img',
            field=models.ImageField(upload_to='historyimgs'),
        ),
    ]
