# Generated by Django 2.1.5 on 2020-03-17 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200315_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(),
        ),
    ]
