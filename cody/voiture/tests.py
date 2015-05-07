# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class VoitureTests(APITestCase):
    fixtures = ['voitures.json']

    def test_get_voiture(self):
        """
        Ensure we can get a existing voiture object.
        """
        url = reverse('voiture:detail', args=(1,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'cylindree': u'1,8 l',
            'description': u'',
            'photo': None,
            'marque': u'Renault',
            'proprietaire': u'Tanguy de Montigny',
            'annee': None,
            'id': 1
        })
