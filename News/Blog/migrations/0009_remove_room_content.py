# Generated by Django 4.0.2 on 2022-04-30 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_remove_room_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='content',
        ),
    ]