# Generated by Django 4.0.1 on 2022-08-01 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_alter_tguser_tg_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tguser',
            name='tg_chat_id',
            field=models.BigIntegerField(blank=True, default=None, null=True, verbose_name='Telegram Chat ID'),
        ),
    ]
