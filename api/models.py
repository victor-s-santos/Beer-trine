from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class BeerSchool(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "school"
        verbose_name_plural = "schools"


class BeerHop(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "hop"
        verbose_name_plural = "hops"


class BeerFamily(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "family"
        verbose_name_plural = "families"


class BeerYeast(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "yeast"
        verbose_name_plural = "yeasts"


class BeerFiltering(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "filterings"
        verbose_name_plural = "filtrations"


class BeerCereal(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "cereal"
        verbose_name_plural = "cereals"


# To Do - use abstract models to avoid repetition in cereals, family, yeast, filtering


class Beer(models.Model):
    name = models.CharField(max_length=200)
    water_percentage = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    school = models.ForeignKey(BeerSchool, on_delete=models.SET_NULL, null=True)
    hops = models.ForeignKey(BeerHop, on_delete=models.SET_NULL, null=True)
    family = models.ForeignKey(BeerFamily, on_delete=models.SET_NULL, null=True)
    yeast = models.ForeignKey(BeerYeast, on_delete=models.SET_NULL, null=True)
    filtering = models.ForeignKey(
        BeerFiltering, on_delete=models.SET_NULL, null=True
    )
    cereals = models.ManyToManyField(BeerCereal)

    class Meta:
        verbose_name = "beer"
        verbose_name_plural = "beers"
