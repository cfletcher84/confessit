# Generated by Django 5.1.1 on 2024-09-16 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confessit_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='name',
            new_name='username',
        ),
    ]
