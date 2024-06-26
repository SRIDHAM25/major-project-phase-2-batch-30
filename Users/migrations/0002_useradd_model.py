# Generated by Django 2.0.5 on 2019-02-27 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAdd_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('dept', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('website', models.CharField(max_length=1000)),
                ('method', models.CharField(max_length=100)),
                ('record', models.CharField(max_length=500)),
                ('attackresult', models.CharField(max_length=500)),
                ('uregid', models.ForeignKey(on_delete='cascade', to='Users.Userregister_Model')),
            ],
        ),
    ]
