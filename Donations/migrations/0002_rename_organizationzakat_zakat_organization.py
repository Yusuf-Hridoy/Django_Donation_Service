# Generated by Django 3.2.12 on 2022-02-22 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zakat',
            old_name='organizationZakat',
            new_name='organization',
        ),
    ]
