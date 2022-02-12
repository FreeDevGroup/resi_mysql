# Generated by Django 4.0.2 on 2022-02-11 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('proprio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noteresidence',
            name='idresidence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proprio.residence'),
        ),
        migrations.AddField(
            model_name='commande',
            name='idclient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client'),
        ),
        migrations.AddField(
            model_name='commande',
            name='idresidence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proprio.residence'),
        ),
        migrations.AddField(
            model_name='ajoutdesejour',
            name='idcommande',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.commande'),
        ),
    ]
