# Generated by Django 2.2.6 on 2019-10-19 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20191017_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrescriptionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('images', models.FileField(upload_to='prescription/')),
            ],
        ),
    ]
