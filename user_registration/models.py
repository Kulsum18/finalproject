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

class RegistrationData(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    nama_lengkap = models.CharField(max_length=50)
    tgl_lahir = models.DateField('Birthday')
    jenis_kelamin = models.CharField(max_length=1, choices=SEX_CHOICES)
    alamat = models.TextField()
    no_hp = models.IntegerField()
    email = models.EmailField('Email', max_length=100, unique=True)
    id_instagram = models.CharField(max_length=50)
    fb_url = models.URLField()
    web_portofolio_url = models.URLField()
    pekerjaan = models.CharField(max_length=15, choices=JOB_CHOICES)
    bidang_desain = models.CharField(max_length=15, choices=BIDANG_DESAIN)
    program_desain = models.CharField(max_length=15, choices=PROGRAM_DESAIN)
    deskripsi_diri = models.TextField()
    tujuan_gabung_bogrades = models.TextField()
    harapan_gabung_bogrades = models.TextField()
    upload_foto_diri = models.ImageField(upload_to="photoprofile/")
    upload_portofolio = models.ImageField(upload_to="portofolio/")

    def __str__(self):
        return self.username

