# Generated by Django 3.2.12 on 2022-03-21 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donations', '0003_delete_requestfordonation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='zakat',
            name='date',
            field=models.DateField(),
        ),
    ]
