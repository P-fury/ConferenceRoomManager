# Generated by Django 5.0.2 on 2024-02-09 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoomManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('commentary', models.TextField(blank=True)),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RoomManager.room')),
            ],
        ),
    ]
