# Generated by Django 2.2 on 2019-04-06 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business_rating', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='address',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
