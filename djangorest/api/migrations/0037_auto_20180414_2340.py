# Generated by Django 2.0.2 on 2018-04-14 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_auto_20180414_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlelist',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Articlelist',
        ),
    ]