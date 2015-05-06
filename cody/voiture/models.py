# -*- coding: utf-8 -*-

from django.db import models


class Voiture(models.Model):
    # Could be linked to a Marque table instead if necessary.
    marque = models.CharField(max_length=64)
    annee = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    cylindree = models.CharField(max_length=32, blank=True)
    # Could be split in surname, name or linked to a Proprietaire table
    # if necessary.
    proprietaire = models.CharField(max_length=64)
    # Here we split photos in one directory each month. Can be change to day,
    # etc. in function of the volume.
    photo = models.ImageField(upload_to='photos/%Y-%m', blank=True)

    class Meta:
        verbose_name = u'Voiture'
        verbose_name_plural = u'Voitures'
        ordering = ('marque', 'annee', 'proprietaire')

    def __unicode__(self):
        return (u'{self.marque} ({self.annee}) '
                u'- Propriétaire : {self.proprietaire}').format(self=self)
