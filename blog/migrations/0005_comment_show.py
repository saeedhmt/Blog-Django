# Generated by Django 3.1.4 on 2021-02-01 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210201_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='show',
            field=models.BooleanField(default=False, verbose_name='نمایش'),
        ),
    ]
