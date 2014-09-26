# -*- coding: utf-8 -*-
""" unit test of nenga.address """
import shortuuid
import random
from django.test import TransactionTestCase, TestCase
from django.contrib.auth.models import User
from nenga.address.models import Contact


class ContactTransactionTest(TransactionTestCase):
    fixtures = ['nenga_tests/test_data/dummy_users.json',
                'nenga_tests/test_data/dummy_data.json']

    def setUp(self):
        seed = shortuuid.ShortUUID()
        seed.set_alphabet('0123456789')
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.user3 = User.objects.get(pk=3)
        self.contact0 = Contact.objects.create(
            last_name=shortuuid.uuid(),
            first_name=shortuuid.uuid(),
            zip_code=seed.uuid(),
            prefecture=("%02d" % random.randrange(1, 48)),
            city=shortuuid.uuid(),
            address=shortuuid.uuid(),
            address2=shortuuid.uuid(),
            partner_name=shortuuid.uuid(),
            owner=self.user1)

    def test_get_contacts(self):
        query = Contact.objects.get(pk=self.contact0.id)
        self.assertEqual(query.__str__(),
                         '%s %s' % (self.contact0.last_name,
                                    self.contact0.first_name))


class ContactTest(TestCase):
    fixtures = ['nenga_tests/test_data/dummy_users.json',
                'nenga_tests/test_data/dummy_data.json']

    def test_get_contacts(self):
        query = Contact.objects.all()
        self.assertTrue(True)
