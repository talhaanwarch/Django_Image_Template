# Generated by Django 3.0.8 on 2020-07-17 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_classification',
            name='pic',
            field=models.ImageField(upload_to=''),
        ),
    ]
