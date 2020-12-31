# Generated by Django 3.1.4 on 2020-12-31 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='comment',
            field=models.CharField(default='bhains', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='Profile_Pics'),
        ),
    ]