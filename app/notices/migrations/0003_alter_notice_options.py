# Generated by Django 4.0.2 on 2022-02-19 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0002_notice_house'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ['-writed_at']},
        ),
    ]
