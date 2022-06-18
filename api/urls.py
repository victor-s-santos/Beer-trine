from django.urls import path

from api.views import (
    BeerCerealListCreateView,
    BeerFamilyListCreateView,
    BeerFilteringListCreateView,
    BeerHopListCreateView,
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
    path(
        "beerhop",
        BeerHopListCreateView.as_view(),
        name="beerhoplistcreate",
    ),
]
