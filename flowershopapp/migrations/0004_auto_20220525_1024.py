# Generated by Django 3.2.5 on 2022-05-25 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flowershopapp', '0003_auto_20220525_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flower',
            name='place',
        ),
        migrations.AddField(
            model_name='flower',
            name='place',
            field=models.OneToOneField(default=11, on_delete=django.db.models.deletion.CASCADE, to='flowershopapp.place'),
            preserve_default=False,
        ),
    ]
