# Generated by Django 3.2 on 2021-04-18 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_handwrittendigit_guess'),
    ]

    operations = [
        migrations.AddField(
            model_name='handwrittendigit',
            name='url',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]