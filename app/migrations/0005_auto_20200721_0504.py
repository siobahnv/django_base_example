# Generated by Django 2.2.14 on 2020-07-21 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200721_0409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='hole',
        ),
        migrations.AddField(
            model_name='birdie',
            name='hole',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18')], default='1', max_length=2, null=True),
        ),
    ]
