# Generated by Django 3.1.7 on 2021-04-28 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0004_ad_tutor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad_tutor',
            name='expected_salary',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
