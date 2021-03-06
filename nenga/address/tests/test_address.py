# -*- coding: utf-8 -*-
"""unit test of nenga.address."""
import shortuuid
import random
from django.test import TransactionTestCase, TestCase
from django.contrib.auth.models import User
from nenga.address.models import Contact


class ContactTransactionTest(TransactionTestCase):

    """Unit test of transaction of Contact."""

    fixtures = ['nenga/address/tests/dummy_users.json',
                'nenga/address/tests/dummy_data.json']

    def setUp(self):
        """initialize."""
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

    def test_get_contact(self):
        """unit test get_contacts."""
        query = Contact.objects.get(pk=self.contact0.id)
        self.assertEqual(query.__str__(),
                         '%s %s' % (self.contact0.last_name,
                                    self.contact0.first_name))


class ContactTest(TestCase):

    """unit test Contact."""

    fixtures = ['nenga/address/tests/dummy_users.json',
                'nenga/address/tests/dummy_data.json']

    def test_get_contacts(self):
        """unit test get_contacts."""
        self.assertEqual(len(Contact.objects.all()), 20)
