# Generated by Django 2.2.4 on 2019-09-14 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinyin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userinput',
            table='user_input',
        ),
    ]