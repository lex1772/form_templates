# Generated by Django 4.1.13 on 2023-11-14 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название шаблона')),
                ('date', models.CharField(blank=True, max_length=128, null=True, verbose_name='Дата')),
                ('telephone', models.CharField(blank=True, max_length=128, null=True, verbose_name='Телефон')),
                ('email', models.CharField(blank=True, max_length=128, null=True, verbose_name='Электронная почта')),
                ('text', models.CharField(blank=True, max_length=128, null=True, verbose_name='Текст')),
            ],
        ),
    ]
