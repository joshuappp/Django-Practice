# Generated by Django 2.1.5 on 2020-03-15 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='feature',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
