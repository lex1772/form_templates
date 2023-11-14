import re
from datetime import datetime

from rest_framework.response import Response

from templates.models import Template


def check_for_template(data: dict):
    """Функция для обработки ввода пользователя.
    Получает на вход словарь из ключей и значений query params"""
    response_dict = {}
    for element in data:
        date = ''
        for form in ('%Y-%m-%d', '%d-%m-%Y'):
            try:
                date = datetime.strptime(data[element], form)
            except ValueError:
                pass
            else:
                response_dict[element] = 'date'
        if date == '':
            if re.fullmatch(
                    r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$',
                    data[element]):
                response_dict[element] = 'telephone'
            else:
                if re.fullmatch(
                        r'^[a-zA-Z0-9]{1,100}[@][a-z]{0,10}\.[a-z]{2,4}',
                        data[element]):
                    response_dict[element] = 'email'
                else:
                    response_dict[element] = 'text'

    try:
        name = Template.objects.get(
            **{v: k for k, v in response_dict.items()}).name
    except Exception:
        return Response(response_dict)
    else:
        return Response({'name': name})
