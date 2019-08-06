from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


class PostPortofolio(models.Model):
    objects = models.Manager()
    published = PublishedManager()

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

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )

    nama_project      = models.CharField(max_length=100, blank=True)
    author            = models.CharField(max_length=50, null=True)
    deskripsi_project = models.TextField()
    bidang_desain     = models.CharField(max_length=15, choices=BIDANG_DESAIN, null=True)
    slug              = models.SlugField(max_length=120)
    created           = models.DateTimeField(auto_now_add=True)
    updated           = models.DateTimeField(auto_now=True)
    status            = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse("portofolio_detail", args=[self.id, self.slug])

class Images(models.Model):
    post = models.ForeignKey(PostPortofolio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="portofolio/", blank=True, null=True)

    def __str__(self):
        return str(self.post.id)

@receiver(pre_save, sender=PostPortofolio)
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].nama_project)
    kwargs['instance'].slug = slug        
