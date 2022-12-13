# Generated by Django 4.1.4 on 2022-12-11 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0004_alter_movie_duration_alter_movie_rating_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="rating",
            field=models.CharField(
                choices=[
                    ("G", "G"),
                    ("PG", "Pg"),
                    ("PG13", "Pg13"),
                    ("R", "R"),
                    ("NC-17", "Nc17"),
                ],
                default="G",
                max_length=20,
            ),
        ),
    ]