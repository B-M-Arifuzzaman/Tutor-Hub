# Generated by Django 2.2.5 on 2021-05-01 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210427_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, default='defaultimage.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='profile_pic',
            field=models.ImageField(blank=True, default='defaultimage.jpg', null=True, upload_to=''),
        ),
    ]
