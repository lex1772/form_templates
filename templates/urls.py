from django.urls import path

from templates.apps import TemplatesConfig
from templates.views import TemplateAPIView, TemplateCreateAPIView

app_name = TemplatesConfig.name

# Отдельные урлы для приложения шаблонов
urlpatterns = [
    path(
        "",
        TemplateAPIView.as_view(),
        name='template'
    ),
    path(
        "create",
        TemplateCreateAPIView.as_view(),
        name='template_create'
    ),
]
