# Generated by Django 2.2 on 2019-12-08 08:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20191208_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.UUIDField(default=uuid.UUID('2eedb737-03fd-4a8e-93ba-1df8a034c9a3'), verbose_name='Token'),
        ),
    ]
