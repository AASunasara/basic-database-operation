# Generated by Django 2.2.2 on 2019-06-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_roll_no',
            field=models.IntegerField(),
        ),
    ]
