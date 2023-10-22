from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ContactMessage  # Import the ContactMessage model
from .serializers import ContactMessageSerializer  # Import the serializer

class ContactFormAPI(APIView):
    def post(self, request):
        # Handle incoming data from the contact form
        serializer = ContactMessageSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the valid data to the ContactMessage model
            serializer.save()

            # Respond with a status message
            return Response({'message': 'Contact form data received and saved successfully'}, status=status.HTTP_201_CREATED)

        # If the data is not valid, return an error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
