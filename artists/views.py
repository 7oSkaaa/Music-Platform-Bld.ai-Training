from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArtistSerializer
from .models import Artist


class ArtistView(APIView):
    
    # return all artists
    def get(self, request):
        serializer = ArtistSerializer(Artist.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    # create a new artist
    def post(self, request):
        try:
            serializer = ArtistSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': 'Invalid Formatted Data!'}, status=status.HTTP_400_BAD_REQUEST)
        
        
class ArtistDetailView(APIView):
    # GET a Artist by id
    def get(self, request, *args, **kwargs):
        try:
            serializer = ArtistSerializer(Artist.objects.get(id=kwargs['pk']))
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Artist.DoesNotExist:
            return Response({'message': 'Artist not found!'}, status=status.HTTP_404_NOT_FOUND)
    
    
    # PUT a Artist by id
    def put(self, request, *args, **kwargs):
        try:
            serializer = ArtistSerializer(Artist.objects.get(id=kwargs['pk']), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Artist.DoesNotExist:
            return Response({'message': 'Artist not found!'}, status=status.HTTP_404_NOT_FOUND)
    
    
    # DELETE a Artist by id
    def delete(self, request, *args, **kwargs):
        try:
            Artist.objects.get(id=kwargs['pk']).delete()
            return Response({'message': 'Artist deleted!'}, status=status.HTTP_200_OK)
        except Artist.DoesNotExist:
            return Response({'message': 'Artist not found!'}, status=status.HTTP_404_NOT_FOUND)