# Generated by Django 4.1 on 2023-11-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_userprofile_login_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='customer_type',
            field=models.CharField(choices=[('ART', 'Art'), ('PHT', 'Photography'), ('ENT', 'Curiosity')], max_length=20, verbose_name='Interested in ?'),
        ),
    ]
