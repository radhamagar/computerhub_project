# Generated by Django 4.2.3 on 2023-07-31 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0002_auto_20230731_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='computerbrands',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='computergeneration',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='computerspecification',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
