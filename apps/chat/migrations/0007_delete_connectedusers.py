# Generated by Django 4.1.4 on 2023-01-27 04:32

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
