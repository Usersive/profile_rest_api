
from rest_framework.views import APIView, status
from rest_framework.response import Response
from profile_api import serializers

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

