# Generated by Django 3.2.11 on 2022-01-26 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_studentdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentDetails',
            new_name='StudentDetail',
        ),
    ]