# Generated by Django 2.0.2 on 2018-03-15 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_remove_gameslist_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameslist',
            name='release_date',
            field=models.CharField(default=11, max_length=10),
            preserve_default=False,
        ),
    ]