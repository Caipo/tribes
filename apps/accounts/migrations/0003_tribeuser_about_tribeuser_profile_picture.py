# Generated by Django 4.1.3 on 2022-12-16 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_tribeuser_tribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribeuser',
            name='about',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tribeuser',
            name='profile_picture',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
