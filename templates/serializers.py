from rest_framework.serializers import ModelSerializer

from templates.models import Template


class TemplateSerializer(ModelSerializer):
    """Сериализатор для модели шаблонов"""

    class Meta:
        model = Template
        fields = ('name', 'date', 'telephone', 'email', 'text')
