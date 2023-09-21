from django.db import models

# Create your models here.
from django.db import models


class Difficulty(models.TextChoices):
    EASY = 'Easy', 'Easy'
    MEDIUM = 'Medium', 'Medium'
    HARD = 'Hard', 'Hard'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sdeproblems(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    difficulty = models.CharField(
        max_length=20,
        choices=Difficulty.choices,
        default=Difficulty.MEDIUM
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
