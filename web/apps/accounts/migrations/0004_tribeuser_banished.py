# Generated by Django 4.1.3 on 2022-12-16 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_tribeuser_about_tribeuser_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribeuser',
            name='banished',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]