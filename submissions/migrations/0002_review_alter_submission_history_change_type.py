# Generated by Django 4.2.6 on 2023-10-19 17:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("submissions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("submission_id", models.IntegerField()),
                ("reviewer_id", models.IntegerField()),
                ("date_reviewed", models.DateField()),
                ("comments", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("approved", "Approved"),
                            ("rejected", "Rejected"),
                        ],
                        default="pending",
                        max_length=10,
                    ),
                ),
            ],
            options={
                "db_table": "reviews",
            },
        ),
        migrations.AlterField(
            model_name="submission_history",
            name="change_type",
            field=models.CharField(
                choices=[
                    ("status", "Status"),
                    ("file", "File"),
                    ("reviewer", "Reviewer"),
                ],
                default="None",
                max_length=10,
            ),
        ),
    ]
