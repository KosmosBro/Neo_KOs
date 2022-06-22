from rest_framework.test import APITestCase
from main.models import Company, Category, Contact, Branch
from django.contrib.auth.models import User

"""
Testing Company API.
"""


class TestCompanyApi(APITestCase):
    @classmethod
    def setUp(cls):
        cls.user = User.objects.create_superuser(username='kosmos_admin', password='1234kosmos_admin')
        cls.company = Company.objects.create(id=2)

    def test_company_api(self):
        self.client.login(username='kosmos_admin', password='1234kosmos_admin')

        url = '/api/company/'

        data = {
            'name': 'title',
            'descriptions': 'sddsd',

        }

        response = self.client.get(url, data=data, format='json')
        self.assertEqual(response.status_code, 200)

    # def test_company_add_api(self):
    #     self.client.login(username='kosmos_admin', password='1234kosmos_admin')
    #
    #     url = '/api/company/'
    #
    #     data = {
    #         'name': 'title',
    #         'descriptions': 'sddd',
    #     }
    #
    #     response = self.client.post(url, data=data, format='json')
    #     self.assertEqual(response.status_code, 201)
    #
    # def test_company_update_api(self):
    #     self.client.login(username='kosmos_admin', password='1234kosmos_admin')
    #
    #     data = {
    #         'name': 'title',
    #         'descriptions': 'Company',
    #
    #     }
    #
    #     response = self.client.put('/api/company/2/', data, format='json')
    #     self.assertEqual(response.status_code, 200)

    def test_company_delete_api(self):
        self.client.login(username='kosmos_admin', password='1234kosmos_admin')

        data = {
            'name': 'Company',
            'descriptions': 'Compadsdny',
        }

        response = self.client.delete('/api/company/2/', data, format='json')
        self.assertEqual(response.status_code, 204)

    def test_company_api_fail(self):
        self.client.login(username='kosmos_admin', password='1234kosmos_admin')

        url = '/api/company/'

        data = {
            'name': '@'
        }

        with self.assertRaises(TypeError):
            Company.objects.create(data, url)


class TestCategoryApi(APITestCase):
    @classmethod
    def setUp(cls):
        cls.user = User.objects.create_superuser(username='kosmos_admin', password='1234kosmos_admin')
        cls.company = Category.objects.create(name='Company', id=2)

    def test_category_api(self):
        self.client.login(username='kosmos_admin', password='1234kosmos_admin')

        url = '/api/category/'

        data = {
            'name': 'title',
            'company': self.company.id
        }

        response = self.client.get(url, data=data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_category_add_api(self):
        self.client.login(username='kosmos_admin', password='1234kosmos_admin')

        url = '/api/category/'

        data = {
            'name': 'title1',
            'company': [self.company.id]
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_category_update_api(self):
        self.client.login(username='kosmos_admin', password='1234kosmos_admin')

        data = {
            'name': 'Company',
            'company': [self.company.id]

        }

        response = self.client.put('/api/category/2/', data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_category_delete_api(self):
        self.client.login(username='kosmos_admin', password='1234kosmos_admin')

        data = {
            'name': 'Company',
            'company': [self.company.id]

        }

        response = self.client.delete('/api/category/2/', data, format='json')
        self.assertEqual(response.status_code, 204)

    def test_category_api_fail(self):
        self.client.login(username='kosmos_admin', password='1234kosmos_admin')

        url = '/api/category/'

        data = {
            'name': '@',
            'company': [self.company.id]

        }

        with self.assertRaises(TypeError):
            Category.objects.create(data, url)


class TestContactApi(APITestCase):
    @classmethod
    def setUp(cls):
        cls.user = User.objects.create_superuser(username='kosmos_admin', password='1234kosmos_admin')
        cls.company = Contact.objects.create(type='Company', id=2)

    def test_contact_api(self):
        self.client.login(username='kosmos_admin', password='1234kosmos_admin')

        url = '/api/contact/'

        data = {
            'type': 'title',
            'value': 'dsdsds'
        }

        response = self.client.get(url, data=data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_contact_add_api(self):
        self.client.login(username='kosmos_admin', password='1234kosmos_admin')

        url = '/api/contact/'

        data = {
            'type': 'title1',
            'value': 'fdsfsdf'
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_contact_update_api(self):
        self.client.login(username='kosmos_admin', password='1234kosmos_admin')

        data = {
            'type': 'Company',
            'value': 'ddsdsd'

        }

        response = self.client.put('/api/contact/2/', data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_contact_delete_api(self):
        self.client.login(username='kosmos_admin', password='1234kosmos_admin')

        data = {
            'type': 'Company',
            'value': 'ddsdsd'

        }

        response = self.client.delete('/api/contact/2/', data, format='json')
        self.assertEqual(response.status_code, 204)

    def test_contact_api_fail(self):
        self.client.login(username='kosmos_admin', password='1234kosmos_admin')

        url = '/api/contact/'

        data = {
            'type': 'Com@$pany',
            'value': 'ddsdsd'

        }

        with self.assertRaises(TypeError):
            Contact.objects.create(data, url)


class TestBranchApi(APITestCase):
    @classmethod
    def setUp(cls):
        cls.user = User.objects.create_superuser(username='kosmos_admin', password='1234kosmos_admin')
        cls.company = Branch.objects.create(id=2)

    def test_branch_api(self):
        self.client.login(username='kosmos_admin', password='1234kosmos_admin')

        url = '/api/branch/'

        data = {
            'latitude': 'title',
            'longitude': 'dsdsds',
            'address': 'dsdsadsasds',
        }

        response = self.client.get(url, data=data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_branch_add_api(self):
        self.client.login(username='kosmos_admin', password='1234kosmos_admin')

        url = '/api/branch/'

        data = {
            'latitude': 'title',
            'longitude': 'dsdsds',
            'address': 'dsdsadsasds',
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_branch_update_api(self):
        self.client.login(username='kosmos_admin', password='1234kosmos_admin')

        data = {
            'latitude': 'title',
            'longitude': 'dsdsds',
            'address': 'dsdsadsasds',

        }

        response = self.client.put('/api/branch/2/', data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_branch_delete_api(self):
        self.client.login(username='kosmos_admin', password='1234kosmos_admin')

        data = {
            'latitude': 'title',
            'longitude': 'dsdsds',
            'address': 'dsdsadsasds',

        }

        response = self.client.delete('/api/branch/2/', data, format='json')
        self.assertEqual(response.status_code, 204)

    def test_branch_api_fail(self):
        self.client.login(username='kosmos_admin', password='1234kosmos_admin')

        url = '/api/contact/'

        data = {
            'latitude': 'title',
            'longitude': 'ds^%%#%$%^$$*dsds',
            'address': 'dsdsadsasds',
        }

        with self.assertRaises(TypeError):
            Branch.objects.create(data, url)
