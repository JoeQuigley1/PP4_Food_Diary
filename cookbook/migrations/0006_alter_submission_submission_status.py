# Generated by Django 3.2.16 on 2022-12-10 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0005_auto_20221208_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submission_status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
    ]