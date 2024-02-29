# Generated by Django 5.0.2 on 2024-02-25 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share_app', '0006_alter_expensestracker_howtosplit'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensestracker',
            name='provideSplit',
            field=models.CharField(blank=True, help_text="Provide amount or percentage value only if 'How to split?' is Exact OR Percetage. Note, The format should be user1:value,user2:value where value will be the amount owed by respective user", max_length=50, verbose_name="Provide split value only if it's not Equal"),
        ),
    ]