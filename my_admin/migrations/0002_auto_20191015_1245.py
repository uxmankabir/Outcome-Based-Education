# Generated by Django 2.2.4 on 2019-10-15 07:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserRole',
        ),
    ]