# Generated by Django 5.1.1 on 2024-09-27 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaginaInicial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secao1_titulo', models.CharField(max_length=150)),
                ('secao1_texto', models.TextField()),
                ('secao2_titulo', models.CharField(max_length=150)),
                ('secao2_texto', models.TextField()),
                ('secao3_titulo', models.CharField(max_length=150)),
                ('secao3_texto', models.TextField()),
            ],
        ),
    ]
