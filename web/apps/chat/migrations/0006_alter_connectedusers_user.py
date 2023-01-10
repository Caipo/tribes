# Generated by Django 4.1.4 on 2023-01-05 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0005_connectedusers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectedusers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='online_user', to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
