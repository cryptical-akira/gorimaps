# Generated by Django 4.1.1 on 2022-10-05 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transl', '0002_alter_multilanguagelongtext_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='History_block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=500)),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transl.multilanguagetextfield')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transl.multilanguagetext')),
            ],
        ),
    ]
