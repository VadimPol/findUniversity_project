# Generated by Django 2.2.7 on 2019-11-06 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191106_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domein',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]