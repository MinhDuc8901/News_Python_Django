# Generated by Django 4.0.2 on 2022-04-30 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_room_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='body',
        ),
    ]
