# Generated by Django 3.1.2 on 2020-12-08 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20201205_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='usn',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Recieved', 'Recieved'), ('Acknowledged', 'Acknowledged')], max_length=200, null=True),
        ),
    ]
