# Generated by Django 2.0.5 on 2019-02-27 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_useradd_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useradd_model',
            name='dept',
            field=models.CharField(max_length=10000),
        ),
    ]