# Generated by Django 3.2.9 on 2021-12-06 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cuenta', '0007_carteraahorro_idperfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carteraahorro',
            name='idPerfil',
        ),
        migrations.AddField(
            model_name='carteraahorro',
            name='Perfil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Cuenta.perfil'),
        ),
    ]
