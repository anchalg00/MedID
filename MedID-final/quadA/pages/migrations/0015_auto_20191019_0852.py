# Generated by Django 2.2.6 on 2019-10-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_reportmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalhistorymodel',
            name='height',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='medicalhistorymodel',
            name='weight',
            field=models.CharField(max_length=4),
        ),
    ]
