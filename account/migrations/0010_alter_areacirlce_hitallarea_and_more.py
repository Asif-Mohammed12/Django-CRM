# Generated by Django 4.0.4 on 2023-01-30 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_areacirlce_delete_area_delete_geeksmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areacirlce',
            name='HitAllArea',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='areacirlce',
            name='HitAllAreaPercentage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='areacirlce',
            name='HitOnceArea',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='areacirlce',
            name='HitOnceAreaPercentage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='areacirlce',
            name='OneCircleArea',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='areacirlce',
            name='OverlapArea',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='areacirlce',
            name='OverlapAreaPercentage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='areacirlce',
            name='TotalArea',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='areacirlce',
            name='UntouchedArea',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='areacirlce',
            name='UntouchedAreaPercentage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='areacirlce',
            name='radius',
            field=models.IntegerField(),
        ),
    ]
