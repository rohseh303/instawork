# Generated by Django 4.2.7 on 2023-12-04 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_teammember_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='phone_number',
            field=models.CharField(max_length=13),
        ),
    ]
