# Generated by Django 2.2.19 on 2021-03-11 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('certificates', '0002_auto_20210308_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='created_by',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='certificate',
            name='modified_by',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='certificate',
            name='description',
            field=models.TextField(),
        ),
    ]