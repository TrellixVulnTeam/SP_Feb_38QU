# Generated by Django 2.0.2 on 2018-05-09 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0063_auto_20180509_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleslist',
            name='content1',
            field=models.CharField(default='ytu', max_length=10000),
        ),
        migrations.AlterField(
            model_name='articleslist',
            name='content2',
            field=models.CharField(default='u', max_length=10000),
        ),
        migrations.AlterField(
            model_name='articleslist',
            name='content3',
            field=models.CharField(default='ytu', max_length=10000),
        ),
        migrations.AlterField(
            model_name='articleslist',
            name='content4',
            field=models.CharField(default='tyu', max_length=10000),
        ),
    ]
