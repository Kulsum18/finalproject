# Generated by Django 2.2.3 on 2019-08-06 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20190806_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='position',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
