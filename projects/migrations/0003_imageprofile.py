# Generated by Django 2.2.3 on 2019-07-16 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190716_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('profileimage', models.FilePathField(path='/photoprofile')),
            ],
        ),
    ]
