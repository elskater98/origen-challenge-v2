# Generated by Django 3.1.3 on 2020-11-28 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_editsessionallowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editsessionallowed',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
