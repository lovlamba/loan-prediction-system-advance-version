# Generated by Django 3.1.2 on 2021-10-14 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Loan_Id', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Married', models.CharField(max_length=3)),
                ('Graduated', models.CharField(max_length=3)),
                ('Montly_Income', models.IntegerField()),
                ('Loan_Amount', models.IntegerField()),
                ('Loan_Period', models.IntegerField()),
                ('Credit_Score', models.CharField(max_length=10)),
                ('Loan_status', models.CharField(max_length=100)),
            ],
        ),
    ]
