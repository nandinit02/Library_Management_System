# Generated by Django 3.1.2 on 2021-01-23 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20210117_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower',
            name='status',
            field=models.CharField(blank=True, choices=[('d', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='d', help_text='Book availability', max_length=1),
        ),
    ]
