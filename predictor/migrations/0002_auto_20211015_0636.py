# Generated by Django 3.1.2 on 2021-10-15 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='Credit_Score',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='record',
            name='Graduated',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='record',
            name='Married',
            field=models.CharField(max_length=100),
        ),
    ]