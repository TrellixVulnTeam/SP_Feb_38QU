# Generated by Django 2.0.2 on 2018-05-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0056_auto_20180509_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleslist',
            name='content1',
            field=models.CharField(default=None, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='articleslist',
            name='content2',
            field=models.CharField(default=None, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='articleslist',
            name='content3',
            field=models.CharField(default=None, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='articleslist',
            name='content4',
            field=models.CharField(default=None, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='newslist',
            name='content1',
            field=models.CharField(default=None, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='newslist',
            name='content2',
            field=models.CharField(default=None, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='newslist',
            name='content3',
            field=models.CharField(default=None, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='newslist',
            name='content4',
            field=models.CharField(default=None, max_length=10000, null=True),
        ),
    ]
