# Generated by Django 4.2.1 on 2023-08-11 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metamesh', '0022_alter_event_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='banner',
            field=models.ImageField(blank=True, default='', upload_to='banner'),
        ),
    ]