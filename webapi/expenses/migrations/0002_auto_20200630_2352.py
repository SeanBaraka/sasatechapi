# Generated by Django 3.0.7 on 2020-06-30 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='frequency',
            field=models.CharField(choices=[('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly')], max_length=100),
        ),
    ]
