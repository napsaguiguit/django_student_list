# Generated by Django 3.0.6 on 2020-05-18 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_list', '0007_auto_20200518_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='course',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='list',
            name='gender',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='list',
            name='yearlevel',
            field=models.CharField(max_length=200),
        ),
    ]
