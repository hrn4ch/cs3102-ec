# Generated by Django 2.0.13 on 2019-04-16 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20190415_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='postURL',
            field=models.URLField(default='#'),
        ),
    ]
