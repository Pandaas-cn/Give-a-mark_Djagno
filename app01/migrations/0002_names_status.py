# Generated by Django 2.2 on 2020-04-25 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='names',
            name='status',
            field=models.CharField(default='未答辩', max_length=6),
        ),
    ]
