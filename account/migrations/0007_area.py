# Generated by Django 4.0.4 on 2023-01-24 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_order_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalarea', models.IntegerField()),
                ('hitallarea', models.IntegerField()),
                ('hitoncearea', models.IntegerField()),
                ('overlaparea', models.IntegerField()),
                ('untocuhed', models.IntegerField()),
            ],
        ),
    ]