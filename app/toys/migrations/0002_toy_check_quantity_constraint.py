# Generated by Django 4.2.3 on 2023-07-29 09:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("toys", "0001_initial"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="toy",
            constraint=models.CheckConstraint(
                check=models.Q(("quantity__gte", 0)), name="check_quantity_constraint"
            ),
        ),
    ]
