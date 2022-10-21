# Generated by Django 4.1.1 on 2022-10-21 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gori', '0025_pinedpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='pinedpost',
            name='pined_video_post_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videopost1', to='gori.video'),
        ),
        migrations.AddField(
            model_name='pinedpost',
            name='pined_video_post_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videopost2', to='gori.video'),
        ),
        migrations.AddField(
            model_name='pinedpost',
            name='pined_video_post_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videopost3', to='gori.video'),
        ),
    ]
