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
        fields = "__all__"


class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = "__all__"


class BeerFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerFamily
        fields = "__all__"


class BeerFilteringSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerFiltering
        fields = "__all__"


class BeerHopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerHop
        fields = "__all__"


class BeerSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerSchool
        fields = "__all__"


class BeerYeastSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerYeast
        fields = "__all__"
