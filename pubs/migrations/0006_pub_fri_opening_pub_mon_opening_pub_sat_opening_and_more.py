# Generated by Django 4.2.21 on 2025-06-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubs', '0005_alter_pub_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pub',
            name='fri_opening',
            field=models.CharField(default='Closed', max_length=254),
        ),
        migrations.AddField(
            model_name='pub',
            name='mon_opening',
            field=models.CharField(default='Closed', max_length=254),
        ),
        migrations.AddField(
            model_name='pub',
            name='sat_opening',
            field=models.CharField(default='Closed', max_length=254),
        ),
        migrations.AddField(
            model_name='pub',
            name='sun_opening',
            field=models.CharField(default='Closed', max_length=254),
        ),
        migrations.AddField(
            model_name='pub',
            name='thurs_opening',
            field=models.CharField(default='Closed', max_length=254),
        ),
        migrations.AddField(
            model_name='pub',
            name='tues_opening',
            field=models.CharField(default='Closed', max_length=254),
        ),
        migrations.AddField(
            model_name='pub',
            name='wed_opening',
            field=models.CharField(default='Closed', max_length=254),
        ),
    ]
