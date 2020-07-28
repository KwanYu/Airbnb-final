from django.shortcuts import render
from django.views.generic import detail
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Create your views here.
from .models import Airbnb
from .serializers import AirbnbSerializer


class AirbnbViewSet(viewsets.ModelViewSet):
    queryset = Airbnb.objects.all()
    serializer_class = AirbnbSerializer
    permission_classes = (AllowAny, )

    @action(methods=['POST'], detail=True)
    def query(self, request, pk=None, *args, **kwargs):
        if 'name' in request.data:
            airbnb = Airbnb.objects.get(id=pk)
            title = request.data['name']
            host_name = request.data['host_name']
            response = {'message': 'Airbnb can be queried'}
            return response
            # return Response{ response, status = status.HTTP_200_OK}
