from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50)
    nama_lengkap = forms.CharField(max_length=50)
    password = forms.CharField(max_length=10)
    password_repeat = forms.CharField(max_length=10)
    tgl_lahir = forms.DateField()
    SEX_CHOICES = (('Laki-laki', 'Laki-laki'),('Perempuan','Perempuan'),)
    jenis_kelammin = forms.ChoiceField(choices=SEX_CHOICES)
    alamat = forms.CharField(widget=forms.Textarea)
    no_hp = forms.IntegerField()
    email = forms.EmailField(max_length=100)
    id_instagram = forms.CharField(max_length=50)
    fb_url = forms.CharField(max_length=50)
    web_portofolio_url = forms.CharField(max_length=50)
    JOB_CHOICES = (
        ('Pelajar/Mahasiswa','Pelajar/Mahasiswa'),
        ('Freelance','Freelance'),
        ('Karyawan','Karyawan'),
        ('Belum Bekerja','Belum Bekerja'),
        ('Tenaga Ahli','Tenaga Ahli'),
        ('','Lain-lain'),
    )
    pekerjaan = forms.ChoiceField(choices=JOB_CHOICES)
    bidang_desain = forms.CharField(max_length=150)
    program_desain = forms.CharField(max_length=150)
    deskripsi_diri = forms.CharField(widget=forms.Textarea)
    tujuan_gabung_bogrades = forms.CharField(widget=forms.Textarea)
    harapan_gabung_bogrades = forms.CharField(widget=forms.Textarea)
    upload_foto_diri = forms.FilePathField(path="static/img")
    upload_portofolio = forms.FilePathField(path="static/img")
