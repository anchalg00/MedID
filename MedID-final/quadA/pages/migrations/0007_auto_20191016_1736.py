# Generated by Django 2.2.6 on 2019-10-16 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20191016_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalhistorymodel',
            name='medication',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='medicalhistorymodel',
            name='other_allergy',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='medicalhistorymodel',
            name='other_illness',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
