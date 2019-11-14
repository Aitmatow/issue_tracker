# Generated by Django 2.2 on 2019-11-13 17:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20191113_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='teams', to='webapp.Projects'),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.UUIDField(default=uuid.UUID('41ee75cd-4a1e-4cdf-987e-cb0ad9f1caeb'), verbose_name='Token'),
        ),
    ]
