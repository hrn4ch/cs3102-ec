# Generated by Django 2.1.5 on 2019-02-18 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20190218_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='suggestion',
            field=models.CharField(max_length=500),
        ),
    ]