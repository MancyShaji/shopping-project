from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.

class cat(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def fil_url(self):
        return reverse('pro_ct',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)



class products(models.Model):
    name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    available=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(cat,on_delete=models.CASCADE)


    def __str__(self):
        return '{}'.format(self.name)
