# Generated by Django 4.0.2 on 2022-03-30 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proprio', '0002_remove_proprietaire_password_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='residence',
            old_name='disponibilité',
            new_name='disponibilite',
        ),
    ]
