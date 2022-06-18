from django.urls import path

from api.views import (
    BeerCerealListCreateView,
    BeerFamilyListCreateView,
    BeerFilteringListCreateView,
)


urlpatterns = [
    path(
        "beercereal",
        BeerCerealListCreateView.as_view(),
        name="beercereallistcreate",
    ),
    path(
        "beerfamily",
        BeerFamilyListCreateView.as_view(),
        name="beerfamilylistcreate",
    ),
    path(
        "beerfiltering",
        BeerFilteringListCreateView.as_view(),
        name="beerfilteringlistcreate",
    ),
]
