# Generated by Django 2.1 on 2018-08-04 00:35

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
    ]
