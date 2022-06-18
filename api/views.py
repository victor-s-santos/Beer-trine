from email.policy import HTTP

from rest_framework import generics, status
from rest_framework.response import Response

from api.models import (
    Beer,
    BeerCereal,
    BeerFamily,
    BeerFiltering,
    BeerHop,
    BeerSchool,
    BeerYeast,
)
from api.serializers import (
    BeerCerealSerializer,
    BeerFamilySerializer,
    BeerFilteringSerializer,
    BeerHopSerializer,
    BeerSchoolSerializer,
    BeerSerializer,
    BeerYeastSerializer,
)


class BeerCerealListCreateView(generics.ListCreateAPIView):
    def get(self, request: dict) -> Response:
        queryset = BeerCereal.objects.all()
        serializer_class = BeerCerealSerializer(queryset, many=True)
        if len(serializer_class.data) == 0:
            return Response(
                "There are no BeerCereal recorded.", status=status.HTTP_200_OK
            )
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def post(self, request: dict) -> Response:
        serializer_class = BeerCerealSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(
                serializer_class.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer_class.errors, status=status.HTTP_400_BAD_REQUEST
        )


class BeerCerealRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView
):
    def get(self, request: dict, beer_id: int = None) -> Response:
        try:
            beer_cereal_detail = BeerCereal.objects.get(id=beer_id)
        except BeerCereal.DoesNotExist:
            return Response(
                "BeerCereal does not exist.", status=status.HTTP_400_BAD_REQUEST
            )
        serializer_class = BeerCerealSerializer(beer_cereal_detail, many=False)
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def patch(self, request: dict, beer_id: int = None) -> Response:
        try:
            beer_cereal_detail = BeerCereal.objects.get(id=beer_id)
        except BeerCereal.DoesNotExist:
            return Response(
                "BeerCereal does not exist.", status=status.HTTP_400_BAD_REQUEST
            )
        context = {
            "name": request.query_params.get("name", None)
            or BeerCereal.objects.get(id=beer_id).name,
            "descritpion": request.query_params.get("description", None)
            or BeerCereal.objects.get(id=beer_id).description,
        }
        serializer_class = BeerCerealSerializer(
            beer_cereal_detail, data=request.data, partial=True
        )
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(
                serializer_class.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer_class.errors, status=status.HTTP_400_BAD_REQUEST
        )


class BeerFamilyListCreateView(generics.ListCreateAPIView):
    def get(self, request: dict) -> Response:
        queryset = BeerFamily.objects.all()
        serializer_class = BeerFamilySerializer(queryset, many=True)
        if len(serializer_class.data) == 0:
            return Response(
                "There are no BeerFamily recorded.", status=status.HTTP_200_OK
            )
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def post(self, request: dict) -> Response:
        serializer_class = BeerFamilySerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(
                serializer_class.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer_class.errors, status=status.HTTP_400_BAD_REQUEST
        )


class BeerFilteringListCreateView(generics.ListCreateAPIView):
    def get(self, request: dict) -> Response:
        queryset = BeerFiltering.objects.all()
        serializer_class = BeerFilteringSerializer(queryset, many=True)
        if len(serializer_class.data) == 0:
            return Response(
                "There are no BeerFiltering recorded.",
                status=status.HTTP_200_OK,
            )
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def post(self, request: dict) -> Response:
        serializer_class = BeerFilteringSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(
                serializer_class.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer_class.errors, status=status.HTTP_400_BAD_REQUEST
        )


class BeerHopListCreateView(generics.ListCreateAPIView):
    def get(self, request: dict) -> Response:
        queryset = BeerHop.objects.all()
        serializer_class = BeerHopSerializer(queryset, many=True)
        if len(serializer_class.data) == 0:
            return Response(
                "There are no BeerHop recorded.",
                status=status.HTTP_200_OK,
            )
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def post(self, request: dict) -> Response:
        serializer_class = BeerHopSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(
                serializer_class.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer_class.errors, status=status.HTTP_400_BAD_REQUEST
        )


class BeerSchoolListCreateView(generics.ListCreateAPIView):
    def get(self, request: dict) -> Response:
        queryset = BeerSchool.objects.all()
        serializer_class = BeerSchoolSerializer(queryset, many=True)
        if len(serializer_class.data) == 0:
            return Response(
                "There are no BeerSchool recorded.",
                status=status.HTTP_200_OK,
            )
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def post(self, request: dict) -> Response:
        serializer_class = BeerSchoolSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(
                serializer_class.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer_class.errors, status=status.HTTP_400_BAD_REQUEST
        )


class BeerYeastListCreateView(generics.ListCreateAPIView):
    def get(self, request: dict) -> Response:
        queryset = BeerYeast.objects.all()
        serializer_class = BeerYeastSerializer(queryset, many=True)
        if len(serializer_class.data) == 0:
            return Response(
                "There are no BeerYeast recorded.",
                status=status.HTTP_200_OK,
            )
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def post(self, request: dict) -> Response:
        serializer_class = BeerYeastSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(
                serializer_class.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer_class.errors, status=status.HTTP_400_BAD_REQUEST
        )


class BeerListCreateView(generics.ListCreateAPIView):
    def get(self, request: dict) -> Response:
        queryset = Beer.objects.all()
        serializer_class = BeerSerializer(queryset, many=True)
        if len(serializer_class.data) == 0:
            return Response(
                "There are no Beer recorded.",
                status=status.HTTP_200_OK,
            )
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def post(self, request: dict) -> Response:
        serializer_class = BeerSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(
                serializer_class.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer_class.errors, status=status.HTTP_400_BAD_REQUEST
        )
