# Generated by Django 2.0.2 on 2018-05-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_remove_gameslist_user_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleslist',
            name='content',
        ),
        migrations.RemoveField(
            model_name='newslist',
            name='content',
        ),
        migrations.AddField(
            model_name='articleslist',
            name='content1',
            field=models.CharField(default='p1 here', max_length=10000),
        ),
        migrations.AddField(
            model_name='articleslist',
            name='content2',
            field=models.CharField(default='p2 here', max_length=10000),
        ),
        migrations.AddField(
            model_name='articleslist',
            name='content3',
            field=models.CharField(default='p3 here', max_length=10000),
        ),
        migrations.AddField(
            model_name='articleslist',
            name='content4',
            field=models.CharField(default='p4 here', max_length=10000),
        ),
        migrations.AddField(
            model_name='newslist',
            name='content1',
            field=models.CharField(default='p1 here', max_length=10000),
        ),
        migrations.AddField(
            model_name='newslist',
            name='content2',
            field=models.CharField(default='p2 here', max_length=10000),
        ),
        migrations.AddField(
            model_name='newslist',
            name='content3',
            field=models.CharField(default='p3 here', max_length=10000),
        ),
        migrations.AddField(
            model_name='newslist',
            name='content4',
            field=models.CharField(default='p4 here', max_length=10000),
        ),
    ]
