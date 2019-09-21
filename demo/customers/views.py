from django.contrib.auth.models import User
from rest_framework import views, status, generics
from .serializers import CustomerSerializer
from rest_framework.response import Response


class CustomerListCreateApiView(views.APIView):
    def get(self, request, *args, **kwargs):
        # List of customers
        queryset = User.objects.all()

        # NOTE: NO VALIDATION HERE. IT'S NOT NECESSARY
        serializer = CustomerSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # no customizable interface: perform_create -> business logic not isolated
        serializer.save()  # We can save cause ModelSerializer has an implementation

        # NOTE: Still missing Location header which DRF adds
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomerRetrieveUpdateApiView(views.APIView):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()

        # no lookup arg
        instance = generics.get_object_or_404(queryset, {"id": kwargs["id"]})
        serializer = CustomerSerializer(instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        queryset = User.objects.all()

        # no lookup arg
        instance = generics.get_object_or_404(queryset, {"id": kwargs["id"]})
        serializer = CustomerSerializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)

        # no customizable interface: perform_update -> business logic not isolated
        serializer.save()

        # no prefetch_related cache invalidation which DRF does

        return Response(serializer.data)
