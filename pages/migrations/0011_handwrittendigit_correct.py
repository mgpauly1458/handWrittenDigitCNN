# Generated by Django 3.2 on 2021-04-24 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20210424_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='handwrittendigit',
            name='correct',
            field=models.BooleanField(default=False),
        ),
    ]