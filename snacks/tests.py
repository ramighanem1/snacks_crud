from django.test import TestCase
from django.urls import reverse
from .models import Snack
from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

class SnackTestCase(TestCase):
    def setUp(self):
        self.purchaser = get_user_model().objects.create(username="tester",email='teas@email.com',password="tester")
        self.snack = Snack.objects.create(
            name='Chips',
            purchaser=self.purchaser,
            description='Delicious chips'
        )

    def test_list_page_status_code(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_detail_page_status_code(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_detail_page_context(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        snack = response.context['snack']
        self.assertEqual(snack.name, "Chips")
        self.assertEqual(snack.description, "Delicious chips")
        self.assertEqual(snack.purchaser.username, "tester")


 


