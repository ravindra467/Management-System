# Generated by Django 2.2.19 on 2021-03-09 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('lecturer_name', models.CharField(blank=True, default='', max_length=100)),
                ('date', models.DateField()),
                ('slides_url', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
