from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class BaseBeer(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        abstract = True


class BeerSchool(BaseBeer):
    class Meta:
        verbose_name = "school"
        verbose_name_plural = "schools"


class BeerHop(BaseBeer):
    class Meta:
        verbose_name = "hop"
        verbose_name_plural = "hops"


class BeerFamily(BaseBeer):
    class Meta:
        verbose_name = "family"
        verbose_name_plural = "families"


class BeerYeast(BaseBeer):
    class Meta:
        verbose_name = "yeast"
        verbose_name_plural = "yeasts"


class BeerFiltering(BaseBeer):
    class Meta:
        verbose_name = "filterings"
        verbose_name_plural = "filtrations"


class BeerCereal(BaseBeer):
    class Meta:
        verbose_name = "cereal"
        verbose_name_plural = "cereals"


class BeerStyle(BaseBeer):
    class Meta:
        verbose_name = "style"
        verbose_name_plural = "styles"


class Beer(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
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
    beerstyle = models.ForeignKey(
        BeerStyle, on_delete=models.SET_NULL, null=True
    )
    cereals = models.ManyToManyField(BeerCereal)

    class Meta:
        verbose_name = "beer"
        verbose_name_plural = "beers"
