# Generated by Django 2.2.3 on 2019-08-05 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostPortofolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_project', models.CharField(max_length=100)),
                ('bidang_desain', models.CharField(choices=[('branding', 'Branding'), ('illustration', 'Illustration'), ('publication', 'Publication'), ('webdesign', 'Web Design'), ('photography', 'Photography'), ('infographic', 'Infographic'), ('mograph', 'Motion Graphic'), ('dgimaging', 'Digital Imaging'), ('typography', 'Typography'), ('wpap', 'WPAP'), ('lettering', 'Lettering'), ('doodle', 'Doodle'), ('mural', 'Mural'), ('drawing', 'drawing'), ('fashiondesign', 'Fashion Design'), ('lain', 'Lain-lain')], max_length=15, null=True)),
                ('slug', models.SlugField(max_length=120)),
                ('deskripsi_project', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='portofolio/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard_user.PostPortofolio')),
            ],
        ),
    ]