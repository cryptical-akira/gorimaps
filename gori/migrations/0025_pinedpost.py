# Generated by Django 4.1.1 on 2022-10-21 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gori', '0024_alter_architect_post_videos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PinedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pined_culture_post_1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='culturepost1', to='gori.culture')),
                ('pined_culture_post_2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='culturepost2', to='gori.culture')),
                ('pined_history_post_1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='historypost1', to='gori.history')),
                ('pined_history_post_2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='historypost2', to='gori.history')),
            ],
        ),
    ]
