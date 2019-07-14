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
    (' ', 'Yang lain:')
)

class PendaftaranMember(models.Model):
    id_anggota = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    nama_lengkap = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    password_repeat = models.CharField(max_length=10)
    tgl_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=1, choices=SEX_CHOICES)
    alamat = models.TextField(max_length=50)
    no_hp = models.IntegerField()
    email = models.EmailField(max_length=100)
    id_instagram = models.CharField(max_length=50)
    fb_url = models.CharField(max_length=50)
    web_portofolio_url = models.CharField(max_length=50)
    pekerjaan = models.CharField(max_length=15, choices=JOB_CHOICES)
    bidang_desain = models.CharField(max_length=150)
    program_desain = models.CharField(max_length=150)
    deskripsi_diri = models.TextField(max_length=500)
    tujuan_gabung_bogrades = models.TextField(max_length=500)
    harapan_gabung_bogrades = models.TextField(max_length=500)
    upload_foto_diri = models.ImageField(upload_to="photoprofile/")
    upload_portofolio = models.ImageField(upload_to="portofolio/")

