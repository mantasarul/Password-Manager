# Generated by Django 3.2.5 on 2021-07-25 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name_plural': 'Accounts'},
        ),
        migrations.AlterModelOptions(
            name='codes',
            options={'verbose_name_plural': 'Codes'},
        ),
        migrations.AlterModelOptions(
            name='email',
            options={'verbose_name_plural': 'Emails'},
        ),
        migrations.AlterModelOptions(
            name='phone',
            options={'verbose_name_plural': 'Phones'},
        ),
    ]