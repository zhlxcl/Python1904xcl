# Generated by Django 2.2.3 on 2019-07-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
