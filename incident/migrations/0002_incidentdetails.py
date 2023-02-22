# Generated by Django 4.1.7 on 2023-02-21 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncidentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_number', models.CharField(max_length=50)),
                ('reporter_name', models.CharField(blank=True, max_length=50, null=True)),
                ('reported_date', models.DateTimeField()),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='----', max_length=100)),
                ('incident_status', models.CharField(choices=[('Open', 'Open'), ('In progress', 'In progress'), ('Closed', 'Closed')], default='Open', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]