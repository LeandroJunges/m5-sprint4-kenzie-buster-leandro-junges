from django.db import models

class Rating(models.TextChoices):
    G = "G"
    PG = "PG"
    PG13 = "PG13"
    R = "R"
    NC17 = "NC-17"

class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(max_length=20, choices= Rating.choices, default=Rating.G)
    synopsis = models.TextField(null=True)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
        
    )
    orders = models.ManyToManyField("users.User", through="movies.MovieOrder", related_name="ordered_movies")

class MovieOrder(models.Model):
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.PROTECT, related_name="movie_order",)
    order = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name= "user_movie_order")

    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2 )


