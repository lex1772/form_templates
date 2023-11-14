from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from templates.serializers import TemplateSerializer
from templates.services import check_for_template


class TemplateAPIView(APIView):
    """Контроллер для получения названия шаблона формы.
    В случае, если форма не найдена, то возвращает типы полей с названиями"""

    def post(self, request):
        """Метод POST, через который проводятся все операции по ТЗ"""
        data = request.GET
        if data == {}:
            return Response("Нет данных")
        return check_for_template(data)


class TemplateCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания шаблона.
    Сделано дополнительно,
    так как в ТЗ не было указано
     как вносить шаблоны от пользователя."""
    serializer_class = TemplateSerializer
