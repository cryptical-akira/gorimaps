# Generated by Django 4.1.1 on 2022-10-23 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gori', '0030_alter_historypin_post_videos_alter_pin_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistoryPin',
            new_name='PostForPin',
        ),
    ]
