# Generated by Django 3.1.7 on 2021-02-23 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_ourworkphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourworkphoto',
            name='image',
        ),
        migrations.AddField(
            model_name='ourworkphoto',
            name='image_after',
            field=models.FileField(null=True, upload_to='ourWork/after'),
        ),
        migrations.AddField(
            model_name='ourworkphoto',
            name='image_before',
            field=models.FileField(null=True, upload_to='ourWork/before'),
        ),
    ]
