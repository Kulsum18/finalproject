# Generated by Django 2.2.3 on 2019-08-06 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postportofolio',
            options={},
        ),
        migrations.AlterField(
            model_name='postportofolio',
            name='author',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='postportofolio',
            name='nama_project',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
