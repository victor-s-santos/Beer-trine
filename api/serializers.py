from rest_framework import serializers

from api.models import (
    Beer,
    BeerCereal,
    BeerFamily,
    BeerFiltering,
    BeerHop,
    BeerSchool,
    BeerYeast,
)


class BeerCerealSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerCereal
        fields = ("name",)


class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = "__all__"


class BeerFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerFamily
        fields = ("name",)


class BeerFilteringSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerFiltering
        fields = ("name",)


class BeerHopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerHop
        fields = ("name",)


class BeerSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerSchool
        fields = ("name",)


class BeerYeastSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerYeast
        fields = ("name",)
