from django.db import models

class Rating(models.TextChoices):
    G = "G"
    PG = "PG"
    PG13 = "PG13"
    R = "R"
    NC17 = "NC-17"

class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True)
    rating = models.CharField(max_length=20, choices= Rating.choices, default=Rating.G)
    synopsis = models.TextField(null=True)
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
        
    )
