# Generated by Django 2.2 on 2019-11-06 04:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20191101_0435'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teams',
            options={'verbose_name': 'Команда', 'verbose_name_plural': 'Команды'},
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.UUIDField(default=uuid.UUID('1b398908-b09a-4f59-ae24-a3736b4190fd'), verbose_name='Token'),
        ),
    ]
