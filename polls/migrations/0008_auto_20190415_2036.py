# Generated by Django 2.0.13 on 2019-04-16 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20190415_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='image',
            field=models.ImageField(default='default-thumbnail.jpg', upload_to=''),
        ),
    ]
