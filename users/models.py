# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
SEX_CHOICES = (
    ('L', 'Laki-laki'),
    ('P', 'Perempuan'),
)

JOB_CHOICES = (
    ('pljr/mhs', 'Pelajar/Mahasiswa'),
    ('freelance', 'Freelance'),
    ('karyawan', 'Karyawan'),
    ('blmbekerja', 'Belum Bekerja'),
    ('tgahli', 'Tenaga Ahli'),
    ('wiraswasta', 'Wiraswasta'),
    ('lain', 'Lain-lain')
)

BIDANG_DESAIN = (
    ('branding', 'Branding'),
    ('illustration', 'Illustration'),
    ('publication', 'Publication'),
    ('webdesign', 'Web Design'),
    ('photography', 'Photography'),
    ('infographic', 'Infographic'),
    ('mograph', 'Motion Graphic'),
    ('dgimaging', 'Digital Imaging'),
    ('typography', 'Typography'),
    ('wpap', 'WPAP'),
    ('lettering', 'Lettering'),
    ('doodle', 'Doodle'),
    ('mural', 'Mural'),
    ('drawing', 'drawing'),
    ('fashiondesign', 'Fashion Design'),
    ('lain', 'Lain-lain'),
)

PROGRAM_DESAIN = (
    ('manual', 'Manual'),
    ('ps', 'Adobe Photoshop'),
    ('ai', 'Adobe Illustrator'),
    ('id', 'Adobe Indesign'),
    ('corel', 'CorelDraw'),
    ('autocad', 'Autocad'),
    ('paint', 'Paint'),
    ('mangastudio', 'Manga Studio'),
    ('quark', 'Quark Xpress'),
    ('3ds', '3D Max'),
    ('ink', 'Inkscape'),
    ('sketchup', 'Google SketchUp'),
    ('macromedia', 'Macromedia Freehand'),
    ('lain', 'Lain-lain'),
)

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    jenis_kelamin = models.CharField(max_length=1, choices=SEX_CHOICES, null=True)
    alamat = models.TextField(null=True)
    no_handphone = models.CharField(max_length=30)
    id_instagram = models.CharField(max_length=50, null=True)
    fb_url = models.URLField(null=True)
    web_portofolio_url = models.URLField(null=True)
    pekerjaan = models.CharField(max_length=15, choices=JOB_CHOICES, null=True)
    bidang_desain = models.CharField(max_length=15, choices=BIDANG_DESAIN, null=True)
    program_desain = models.CharField(max_length=15, choices=PROGRAM_DESAIN, null=True)
    deskripsi_diri = models.TextField(null=True)
    tujuan_gabung_bogrades = models.TextField(null=True)
    harapan_gabung_bogrades = models.TextField(null=True)


    def __str__(self):
        return self.email
