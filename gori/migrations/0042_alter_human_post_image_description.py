# Generated by Django 4.1.1 on 2022-10-27 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transl', '0003_alter_multilanguagetext_text_en_and_more'),
        ('gori', '0041_human_post_image_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='post_image_description',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='humanimgdescription', to='transl.multilanguagetextfield'),
        ),
    ]