# Generated by Django 4.2.1 on 2023-08-07 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metamesh', '0012_students_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='club',
            fields=[
                ('clubname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('clubtype', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=200, null=True)),
                ('rules', models.CharField(max_length=200)),
                ('adminname', models.CharField(max_length=100)),
                ('adminid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metamesh.students')),
            ],
            options={
                'db_table': 'club',
            },
        ),
    ]