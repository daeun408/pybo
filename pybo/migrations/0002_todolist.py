# Generated by Django 4.1 on 2023-07-21 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=200)),
                ('end_date', models.DateField()),
                ('done', models.BooleanField()),
            ],
        ),
    ]
