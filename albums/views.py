from rest_framework import generics, mixins, pagination, permissions, status
from rest_framework.response import Response
from .serializers import AlbumSerializer
from .models import Album
from .filters import AlbumFilters
import sys


class AlbumView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = pagination.LimitOffsetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = AlbumFilters
    
    
    # return all albums
    def get(self, request):
        return self.list(request)
    

    def perform_create(self, serializer):
        serializer.save(artist = self.request.user.artist)

    
    # create a new album
    def post(self, request):
        if not hasattr(request.user, 'artist'):
            return Response(status=status.HTTP_403_FORBIDDEN, data={'message':'You must be an artist to create an album'})
        serializer = AlbumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
class AlbumFilterView(generics.ListAPIView):
    
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_class = AlbumFilters
    
    
    def get(self, request, *args, **kwargs):
        params = request.query_params
        gte, lte, icontains = 0, sys.maxsize, ''
        if 'cost__gte' in params:
            if params['cost__gte']:
                try:
                    data = int(params['cost__gte'])
                    gte = data
                except:
                    return Response(data={"cost__gte": [ "Enter a number."]}, status=status.HTTP_400_BAD_REQUEST)

        if 'cost__lte' in params:
            if params['cost__lte']:
                try:
                    data = int(params['cost__lte'])
                    lte = data
                except:
                    return Response(data={"cost__lte": [ "Enter a number."]}, status=status.HTTP_400_BAD_REQUEST)
        
        if 'name__icontains' in params:
            if params['name__icontains']:
                icontains = params['name__icontains']

        data = Album.objects.filter(cost__gte=gte, cost__lte=lte, name__icontains=icontains)
        serializer = AlbumSerializer(data, many=True)

        if 'limit' not in params:
            return Response(serializer.data)
        
        return self.get_paginated_response(self.paginate_queryset(serializer.data))