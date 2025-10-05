from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class PrivateDataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        content = {
            'message': f'Witaj, {user.username}! To są Twoje prywatne dane.',
            'username': user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "groups": [group.name for group in user.groups.all()]
            }
        return Response(content)