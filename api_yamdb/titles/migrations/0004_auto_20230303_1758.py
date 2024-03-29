# Generated by Django 3.2 on 2023-03-03 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0003_auto_20230301_1623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='genres',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='title',
            name='rating',
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
