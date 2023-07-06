from django.db import models


class Recipe(models.Model):
    RECIPE_TITLE_MAX_LENGTH = 30
    INGREDIENTS_MAX_LENGTH = 250

    title = models.CharField(
        max_length=RECIPE_TITLE_MAX_LENGTH,
    )

    image_url = models.URLField()

    description = models.TextField()

    ingredients = models.CharField(
        max_length=INGREDIENTS_MAX_LENGTH,
    )

    time = models.IntegerField(
        verbose_name='Time (Minutes)',
    )

    class Meta:
        ordering = ('title',)

