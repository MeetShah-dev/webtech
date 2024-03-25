# Generated by Django 5.0.3 on 2024-03-25 19:17

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "db_table": "category",
            },
        ),
        migrations.CreateModel(
            name="EmailNotification",
            fields=[
                (
                    "email",
                    models.EmailField(
                        max_length=254, primary_key=True, serialize=False
                    ),
                ),
                ("id", models.BigIntegerField(unique=True)),
                ("type", models.CharField(max_length=255)),
                ("text", models.TextField(max_length=500)),
                ("success", models.BooleanField()),
            ],
            options={
                "db_table": "email_notification",
            },
        ),
        migrations.CreateModel(
            name="Magazine",
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
                ("title", models.CharField(max_length=255)),
                ("flag", models.CharField(max_length=255)),
                ("date_created", models.DateTimeField()),
                ("date_released", models.DateTimeField()),
            ],
            options={
                "db_table": "magazine",
            },
        ),
        migrations.CreateModel(
            name="Role",
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
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "role",
            },
        ),
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField(max_length=5000)),
                ("is_approved", models.BooleanField(default=False)),
                ("is_draft", models.BooleanField(default=False)),
                ("is_ready", models.BooleanField()),
                ("is_rejected", models.BooleanField(default=False)),
                ("rejection_number", models.IntegerField(default=0)),
                ("date_created", models.DateTimeField()),
                ("date_updated", models.DateTimeField(blank=True, null=True)),
                (
                    "reader_ids",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=100),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "keywords",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=100),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                ("likes", models.PositiveIntegerField(default=0)),
                ("comments", models.PositiveIntegerField(default=0)),
                ("readers", models.PositiveIntegerField(default=0)),
                (
                    "categories",
                    models.ManyToManyField(
                        related_name="blogs", to="moderatorAdmin.category"
                    ),
                ),
                (
                    "magazine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="moderatorAdmin.magazine",
                    ),
                ),
            ],
            options={
                "db_table": "blog",
                "ordering": ["-date_created"],
            },
        ),
        migrations.CreateModel(
            name="Feedback",
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
                ("content", models.TextField(max_length=500)),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blogs",
                        to="moderatorAdmin.blog",
                    ),
                ),
            ],
            options={
                "db_table": "feedback",
            },
        ),
        migrations.CreateModel(
            name="File",
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
                ("uid", models.UUIDField(editable=False)),
                ("url", models.FileField(upload_to="files/")),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files",
                        to="moderatorAdmin.blog",
                    ),
                ),
            ],
            options={
                "db_table": "file",
            },
        ),
        migrations.CreateModel(
            name="ScheduledJobs",
            fields=[
                ("job_id", models.CharField(primary_key=True, serialize=False)),
                ("magazine_title", models.CharField(max_length=255)),
                ("status", models.CharField(max_length=255)),
                ("updated_time", models.DateTimeField()),
                ("release_date", models.DateTimeField()),
                (
                    "magazine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="moderatorAdmin.magazine",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="email address"
                    ),
                ),
                ("date_of_birth", models.DateField()),
                ("date_created", models.DateField()),
                ("date_updated", models.DateField(blank=True, null=True)),
                ("last_login_date", models.DateField()),
                ("email_notification", models.BooleanField()),
                (
                    "nationality",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("type", models.CharField(max_length=255)),
                ("gender", models.CharField(max_length=255)),
                ("banned", models.BooleanField(default=False)),
                (
                    "role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="moderatorAdmin.role",
                    ),
                ),
            ],
            options={
                "db_table": "user",
            },
        ),
        migrations.CreateModel(
            name="Like",
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
                ("timestamp", models.DateTimeField()),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="moderatorAdmin.blog",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="moderatorAdmin.user",
                    ),
                ),
            ],
            options={
                "db_table": "like",
            },
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("text", models.TextField(max_length=500)),
                ("timestamp", models.DateTimeField()),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="moderatorAdmin.blog",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="moderatorAdmin.user",
                    ),
                ),
            ],
            options={
                "db_table": "comment",
            },
        ),
        migrations.AddField(
            model_name="blog",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="moderatorAdmin.user"
            ),
        ),
        migrations.CreateModel(
            name="AppNotification",
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
                ("type", models.CharField(max_length=255)),
                ("text", models.TextField(max_length=500)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="moderatorAdmin.blog",
                    ),
                ),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiver",
                        to="moderatorAdmin.user",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sender",
                        to="moderatorAdmin.user",
                    ),
                ),
            ],
            options={
                "db_table": "app_notification",
            },
        ),
    ]
