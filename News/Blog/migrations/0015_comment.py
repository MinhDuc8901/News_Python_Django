# Generated by Django 4.0.4 on 2022-05-07 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0014_alter_topic_options_alter_room_topic_delete_topics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Guest', max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Blog.room')),
            ],
        ),
    ]
