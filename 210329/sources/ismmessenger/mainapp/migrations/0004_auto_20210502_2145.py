# Generated by Django 2.2 on 2021-05-02 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210328_1828'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-created'], 'verbose_name': 'сообщение', 'verbose_name_plural': 'сообщения'},
        ),
    ]