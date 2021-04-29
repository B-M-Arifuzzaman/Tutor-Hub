# Generated by Django 3.2 on 2021-04-29 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_reviewandcomment'),
        ('courses', '0005_alter_class_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(blank=True, to='home.Student'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='home.tutor'),
        ),
    ]
