# Generated by Django 3.1.2 on 2022-02-28 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='teachers', to='school.Teacher'),
        ),
    ]
