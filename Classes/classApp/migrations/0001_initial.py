# Generated by Django 3.2.3 on 2021-05-24 10:50

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Course_Number', models.IntegerField()),
                ('Instructor_Name', models.CharField(max_length=50)),
                ('Duration', models.FloatField()),
            ],
            managers=[
                ('classes', django.db.models.manager.Manager()),
            ],
        ),
    ]