# Generated by Django 4.0.2 on 2022-02-11 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commande',
            options={'ordering': ('-datecommande',)},
        ),
    ]
