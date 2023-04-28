from django.test import TestCase
from django.urls import reverse
from .models import Announcements, Category
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase


class Test_Create_Anouncement(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='testcat')
        test_user = User.objects.create_user(
            username='testuser', password='testpass')
        test_announcement = Announcements.objects.create(
            title='testtitle',
            author_id=1,
            category_id=1,
            lastupdated=timezone.now())

    def test_announcement_create(self):
        announce = Announcements.objects.get(id=1)
        cat = Category.objects.get(id=1)
        title = f'{announce.title}'
        author = f'{announce.author}'
        cat = f'{announce.category}'
        self.assertEqual(author, 'testuser')
        self.assertEqual(cat, 'testcat')
        self.assertEqual(title, 'testtitle')
        self.assertEqual(str(announce), 'testtitle')
        self.assertEqual(str(cat), 'testcat')


class Test_Announcements(APITestCase):

    def test_list_announcements(self):
        url = reverse('announcementlist')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)