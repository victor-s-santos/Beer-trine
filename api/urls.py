from django.urls import path
from api.views import BeerListCreateView

urlpatterns = [
    path("", BeerListCreateView.as_view(), name="beerlistcreate"),
]