# Generated by Django 2.0.13 on 2019-04-20 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_auto_20190420_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='icon',
        ),
        migrations.AddField(
            model_name='topic',
            name='imageURL',
            field=models.URLField(default='https://www.templaza.com/blog/components/com_easyblog/themes/wireframe/images/placeholder-image.png'),
        ),
    ]
