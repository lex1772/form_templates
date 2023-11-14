from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from templates.models import Template


class TemplateTestCase(APITestCase):
    # Тесты для форм шаблона
    def setUp(self) -> None:
        # Создание шаблона формы для тестирования

        self.template = Template.objects.create(
            name="My_template",
            date="date",
            telephone="telephone",
            email="email",
            text="text"
        )

    def create_template(self):
        # Тест на создание пользовательского шаблона через API
        data = {
            "name": "Favorite_template",
            "date": "dt",
            "telephone": "tl",
            "email": "em",
            "text": "tx"
        }
        response = self.client.post(
            reverse('template:template_create'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_template(self):
        # Получение шаблона формы
        response = self.client.post(
            reverse(
                'template:template'
            ) + '?date=date&telephone=telephone&email=email&text=text',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'name': 'My_template'})

    def test_get_empty_template(self):
        # Получение пустого шаблона формы
        response = self.client.post(
            reverse('template:template'),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), 'Нет данных')

    def test_not_found_template(self):
        # Получение не найденного шаблона формы
        response = self.client.post(
            reverse(
                'template:template'
            ) + '?dat=01-01-2000&tel=%2B79998889988&email=a@a.ru&txt=text',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'dat': 'date',
             'email': 'email',
             'tel': 'telephone',
             'txt': 'text'
             }
            )
