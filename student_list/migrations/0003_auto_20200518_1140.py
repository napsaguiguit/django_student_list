# Generated by Django 3.0.6 on 2020-05-18 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_list', '0002_list_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='course',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='list',
            name='firstname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='list',
            name='gender',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='list',
            name='lastname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='list',
            name='yearlevel',
            field=models.CharField(max_length=200),
        ),
    ]
