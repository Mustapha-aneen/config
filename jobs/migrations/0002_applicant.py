# Generated by Django 4.2.1 on 2023-09-15 14:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
