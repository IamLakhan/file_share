# Generated by Django 4.0.2 on 2022-04-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usershare',
            name='from_user',
            field=models.CharField(max_length=300),
        ),
    ]