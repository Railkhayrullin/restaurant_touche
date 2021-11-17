from django.db import models
from django.db.models import UniqueConstraint


class Category(models.Model):
    """Категории блюда в меню"""
    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        constraints = [
            UniqueConstraint(fields=['name'], name='unique_category')
        ]

    name = models.CharField("категория", max_length=128)

    def __str__(self):
        return self.name
