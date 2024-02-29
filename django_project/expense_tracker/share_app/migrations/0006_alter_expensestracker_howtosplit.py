# Generated by Django 5.0.2 on 2024-02-25 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share_app', '0005_expensestracker_howtosplit_expesneforgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensestracker',
            name='howtosplit',
            field=models.CharField(choices=[('eq', 'Equal'), ('Ex', 'Exact'), ('Sp', 'Split')], default='Select from below options', max_length=2, verbose_name='How to split?'),
        ),
    ]
