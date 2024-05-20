
from rest_framework.views import APIView, status
from rest_framework.response import Response
from profile_api import serializers
from rest_framework import viewsets

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Return a list of API function"""
        an_apiview =[
            "Uses HTTP method as function (get, put, patch, post, delete)",
            "Is similar to a traditional django view",
            "Give you the most control over application logic",
            "is mapped maunally to URLs"
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response ({'message': message})
            
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST,
                )

    def put(self, request,pk=None):
        """Handle updating an object"""
        return Response({'message': 'PUT'})
    
    def patch(self, request, pk=None):
        """Handle partial updating an object"""
        return Response({'message': 'PATCH'})
    
    def delete(self, request, pk=None):
        """Handle deleting an object"""
        return Response({'message': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    def list(self, request):
        """Return a hello message"""
        a_viewset =[
            'Uses action list(create, update, partial_update, retrieve, destroy)',
            'Automatically map to URLs using Routers',
            'Provide less funtionality code',
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    
    def create(self, request):
        """Create a hello message"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response ({'message': message})
        
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST,
                )
    
    def retrieve(self, request, pk=None):
        """Handle getting an object by IDs"""
        return Response({'hhtp_method': 'GET'})
    
    def update(self, request):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})
    
    def partially_update(self, request, pk=None):
        """Handle getting an object by IDs"""
        return Response({'hhtp_method': 'PATC'})
    
    def destroy(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': "DELETE"})
    