# Generated by Django 4.0.2 on 2022-02-09 01:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', '남성'), ('F', '여성')], max_length=10)),
                ('life_pattern', models.CharField(blank=True, choices=[('AM', '아침형'), ('PM', '저녁형')], max_length=10)),
                ('disposition', models.CharField(blank=True, choices=[('collective', '집단주의'), ('individual', '개인주의')], max_length=10)),
                ('mbti', models.CharField(blank=True, choices=[('INTJ', 'INTJ'), ('\u200bINTP', '\u200bINTP'), ('ENTJ', 'ENTJ'), ('ENTP', 'ENTP'), ('INFJ', 'INFJ'), ('INFP', 'INFP'), ('ENFJ', 'ENFJ'), ('ENFP', 'ENFP'), ('ISTJ', 'ISTJ'), ('ISFJ', 'ISFJ'), ('ESTJ', 'ESTJ'), ('ESFJ', 'ESFJ'), ('ISTP', 'ISTP'), ('ISFP', 'ISFP'), ('ESTP', 'ESTP'), ('ESFP', 'ESFP')], max_length=5)),
                ('message', models.TextField(blank=True, max_length=30)),
                ('house', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='houses.house')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
