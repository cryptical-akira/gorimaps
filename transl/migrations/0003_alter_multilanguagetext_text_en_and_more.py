# Generated by Django 4.1.1 on 2022-10-14 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transl', '0002_alter_multilanguagelongtext_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multilanguagetext',
            name='text_en',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='multilanguagetext',
            name='text_ka',
            field=models.CharField(default='', max_length=120),
        ),
    ]
