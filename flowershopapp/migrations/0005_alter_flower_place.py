# Generated by Django 3.2.5 on 2022-05-25 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flowershopapp', '0004_auto_20220525_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowershopapp.place'),
        ),
    ]
