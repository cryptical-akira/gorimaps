# Generated by Django 4.1.1 on 2022-10-14 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transl', '0002_alter_multilanguagelongtext_slug_and_more'),
        ('gori', '0014_remove_aboutprojectdonors_post_img_first_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_img', models.ImageField(null=True, upload_to='humansimg')),
                ('post_text', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='huamnstext', to='transl.multilanguagetextfield')),
                ('post_title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='humans', to='transl.multilanguagetextfield')),
            ],
        ),
    ]
