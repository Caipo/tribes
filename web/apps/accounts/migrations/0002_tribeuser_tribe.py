# Generated by Django 4.1.3 on 2022-12-16 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribeuser',
            name='tribe',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
