# Generated by Django 5.1.1 on 2024-09-19 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('component1', models.IntegerField()),
                ('component2', models.IntegerField()),
                ('component3', models.IntegerField()),
                ('component4', models.IntegerField()),
                ('component5', models.IntegerField()),
                ('component6', models.IntegerField()),
                ('component7', models.IntegerField()),
                ('avg', models.IntegerField()),
            ],
        ),
    ]
