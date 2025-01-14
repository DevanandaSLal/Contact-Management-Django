# Generated by Django 5.1 on 2024-09-26 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('place', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
    ]
