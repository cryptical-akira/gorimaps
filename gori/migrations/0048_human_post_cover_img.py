# Generated by Django 4.1.1 on 2022-11-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gori', '0047_remove_human_post_cover_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='human',
            name='post_cover_img',
            field=models.ImageField(blank=True, null=True, upload_to='humanscoverimg'),
        ),
    ]