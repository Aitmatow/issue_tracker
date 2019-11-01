# Generated by Django 2.2 on 2019-10-31 14:54

from django.db import migrations

def create_profiles(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Profile = apps.get_model('accounts', 'Profile')
    for user in User.objects.all():
        Profile.objects.get_or_create(user=user)

def delete_profiles(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191031_1329'),
    ]

    operations = [
        migrations.RunPython(create_profiles, delete_profiles)
    ]
