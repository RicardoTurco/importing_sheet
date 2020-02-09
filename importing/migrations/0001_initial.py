# Generated by Django 2.2.9 on 2020-02-09 03:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planilha',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('demanda', models.CharField(max_length=150)),
                ('categoria', models.CharField(max_length=30)),
                ('data', models.DateField()),
                ('nome_pessoa', models.CharField(max_length=150)),
                ('tel_pessoa', models.CharField(blank=True, max_length=50, null=True)),
                ('sexo', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
