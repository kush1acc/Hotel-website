# Generated by Django 4.0 on 2021-12-13 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_rename_contactus_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='name_1',
        ),
    ]
