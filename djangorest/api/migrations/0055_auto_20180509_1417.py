# Generated by Django 2.0.2 on 2018-05-09 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0054_auto_20180509_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleslist',
            name='content1',
            field=models.CharField(blank=True, default=None, max_length=10000),
        ),
        migrations.AlterField(
            model_name='articleslist',
            name='content2',
            field=models.CharField(blank=True, default=None, max_length=10000),
        ),
        migrations.AlterField(
            model_name='articleslist',
            name='content3',
            field=models.CharField(blank=True, default=None, max_length=10000),
        ),
        migrations.AlterField(
            model_name='articleslist',
            name='content4',
            field=models.CharField(blank=True, default=None, max_length=10000),
        ),
        migrations.AlterField(
            model_name='newslist',
            name='content1',
            field=models.CharField(blank=True, default=None, max_length=10000),
        ),
        migrations.AlterField(
            model_name='newslist',
            name='content2',
            field=models.CharField(blank=True, default=None, max_length=10000),
        ),
        migrations.AlterField(
            model_name='newslist',
            name='content3',
            field=models.CharField(blank=True, default=None, max_length=10000),
        ),
        migrations.AlterField(
            model_name='newslist',
            name='content4',
            field=models.CharField(blank=True, default=None, max_length=10000),
        ),
    ]
