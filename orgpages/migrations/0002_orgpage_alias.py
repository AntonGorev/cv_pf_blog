# Generated by Django 3.1.7 on 2021-09-11 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgpage',
            name='alias',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
