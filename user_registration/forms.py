from django import forms

YEARS = [x for x in range(1950, 2050)]


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    nama_lengkap = forms.CharField(max_length=50)
    tgl_lahir = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    SEX_CHOICES = (('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan'),)
    jenis_kelamin = forms.ChoiceField(choices=SEX_CHOICES)
    alamat = forms.CharField(widget=forms.Textarea)
    no_hp = forms.CharField()
    email = forms.EmailField(max_length=100)
    id_instagram = forms.CharField(max_length=50)
    fb_url = forms.CharField(max_length=50)
    web_portofolio_url = forms.CharField(max_length=50)
    JOB_CHOICES = (
        ('pljr/mhs', 'Pelajar/Mahasiswa'),
        ('freelance', 'Freelance'),
        ('karyawan', 'Karyawan'),
        ('blmbekerja', 'Belum Bekerja'),
        ('tgahli', 'Tenaga Ahli'),
        ('wiraswasta', 'Wiraswasta'),
        ('lain', 'Lain-lain')
    )
    pekerjaan = forms.ChoiceField(choices=JOB_CHOICES)
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
    bidang_desain = forms.ChoiceField(choices=BIDANG_DESAIN)
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
    program_desain = forms.ChoiceField(choices=PROGRAM_DESAIN)
    deskripsi_diri = forms.CharField(widget=forms.Textarea)
    tujuan_gabung_bogrades = forms.CharField(widget=forms.Textarea)
    harapan_gabung_bogrades = forms.CharField(widget=forms.Textarea)
    upload_foto_diri = forms.ImageField()
    upload_portofolio = forms.ImageField()