# Generated by Django 4.1.4 on 2023-01-07 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_alter_connectedusers_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ConnectedUsers',
        ),
    ]