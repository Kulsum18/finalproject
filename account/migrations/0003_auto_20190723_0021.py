# Generated by Django 2.2.3 on 2019-07-23 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190716_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountdata',
            name='upload_foto_diri',
        ),
        migrations.RemoveField(
            model_name='accountdata',
            name='upload_portofolio',
        ),
    ]
