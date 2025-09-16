from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class PrivateDataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': f'Witaj, {request.user.username}! To są Twoje prywatne dane.'}
        return Response(content)