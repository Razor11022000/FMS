# Generated by Django 3.1.2 on 2020-11-30 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201129_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='ad_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.student'),
        ),
        migrations.AddField(
            model_name='pay',
            name='fid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.fee'),
        ),
    ]
