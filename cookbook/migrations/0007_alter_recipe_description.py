# Generated by Django 3.2.16 on 2022-12-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0006_alter_submission_submission_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
