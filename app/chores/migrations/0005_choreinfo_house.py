# Generated by Django 4.0.2 on 2022-02-11 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_alter_invite_invitee_alter_invite_inviter'),
        ('chores', '0004_alter_choreinfo_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='choreinfo',
            name='house',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='houses.house'),
            preserve_default=False,
        ),
    ]
