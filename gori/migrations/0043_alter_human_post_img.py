# Generated by Django 4.1.1 on 2022-10-29 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gori', '0042_alter_human_post_image_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='post_img',
            field=models.ImageField(blank=True, default='humansimg/default.jpg', null=True, upload_to='humansimg'),
        ),
    ]