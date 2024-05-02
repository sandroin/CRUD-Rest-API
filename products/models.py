from django.db import models
from django.utils.translation import gettext as _


class Product(models.Model):
    categories = models.ManyToManyField('Category', related_name='products', verbose_name=_('Categories'))
    name = models.CharField(max_length=120, verbose_name=_('Product Name'))
    price = models.DecimalField(max_digits=1000000, decimal_places=2, verbose_name=_('Price'))
    amount = models.IntegerField(verbose_name=_('Amount'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['name']
