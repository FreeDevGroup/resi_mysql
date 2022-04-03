# Generated by Django 4.0.2 on 2022-03-27 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AjoutDeSejour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datefin', models.DateField(null=True)),
                ('versementduclient', models.BooleanField(default=False)),
                ('dateajout', models.DateTimeField(auto_now_add=True)),
                ('statudemande', models.CharField(choices=[('ATTENTE', 'En Attente'), ('VALIDE', 'Validé'), ('ANNULE', 'Annulé')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('prenoms', models.CharField(max_length=75)),
                ('phone', models.CharField(max_length=10)),
                ('photo', models.ImageField(null=True, upload_to='client/image/')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.TextField(max_length=255, null=True)),
                ('user_id', models.IntegerField(null=True, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prixactuel', models.IntegerField()),
                ('datedebut', models.DateField()),
                ('datefin', models.DateField()),
                ('versementduclient', models.BooleanField(default=False)),
                ('cleauclient', models.BooleanField(default=False)),
                ('versementauproprio', models.BooleanField(default=False)),
                ('datecommande', models.DateTimeField(auto_now_add=True)),
                ('statucommande', models.CharField(choices=[('ATTENTE', 'En Attente'), ('VALIDE', 'Validé'), ('ANNULE', 'Annulé')], max_length=100)),
            ],
            options={
                'ordering': ('-datecommande',),
            },
        ),
        migrations.CreateModel(
            name='NoteResidence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (3, '4'), (5, '5')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('idclient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
    ]
