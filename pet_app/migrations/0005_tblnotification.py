# Generated by Django 3.2.5 on 2021-09-07 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_app', '0004_tbldoctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblnotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_id', models.CharField(max_length=50)),
                ('notification', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=90)),
            ],
        ),
    ]
