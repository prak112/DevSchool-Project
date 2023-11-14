# Generated by Django 4.1 on 2023-11-14 15:50

from django.db import migrations, models
from django.contrib.auth import get_user_model
from photostore.models import Customer


def create_customers(apps, schema_editor):
    """
    Creates customers based on existing users and customers.

    Args:
        apps (object): A reference to the apps registry.
        schema_editor (object): A reference to the schema editor.

    Returns:
        None
    """
    # collect existing users
    UserProfile = get_user_model()
    existing_users = UserProfile.objects.all()
    
    # validate if existing users are existing customers
    for user in existing_users:
        existing_customer = Customer.objects.filter(user_info=user).exists()

        if not existing_customer:
            Customer.objects.create(user_info=user)
        


class Migration(migrations.Migration):

    dependencies = [
        ('photostore', '0010_rename_user_type_customer_customer_type'),
    ]

    operations = [
        migrations.RunPython(create_customers),
    ]
