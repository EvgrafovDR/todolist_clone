# Generated by Django 4.0.1 on 2022-08-01 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tguser',
            name='tg_chat_id',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Telegram Chat ID'),
        ),
    ]
