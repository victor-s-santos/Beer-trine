from django.urls import path

from api.views import (
    BeerCerealListCreateView,
    BeerCerealRetrieveUpdateDestroyView,
    BeerFamilyListCreateView,
    BeerFilteringListCreateView,
    BeerHopListCreateView,
    BeerListCreateView,
    BeerSchoolListCreateView,
    BeerStyleListCreateView,
    BeerYeastListCreateView,
)


urlpatterns = [
    path(
        "beercereal",
        BeerCerealListCreateView.as_view(),
        name="beercereallistcreate",
    ),
    path(
        "beercereal/<int:beer_id>/",
        BeerCerealRetrieveUpdateDestroyView.as_view(),
        name="beercerealretrieveupdatedestroy",
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
    path(
        "beerschool",
        BeerSchoolListCreateView.as_view(),
        name="beerschoollistcreate",
    ),
    path(
        "beerstyle",
        BeerStyleListCreateView.as_view(),
        name="beerstylelistcreate",
    ),
    path(
        "beeryeast",
        BeerYeastListCreateView.as_view(),
        name="beeryeastlistcreate",
    ),
    path(
        "beer",
        BeerListCreateView.as_view(),
        name="beerlistcreate",
    ),
]
