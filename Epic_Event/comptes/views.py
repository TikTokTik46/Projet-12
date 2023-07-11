from rest_framework.response import Response
from comptes.serializers import UserSerializer
from rest_framework import status
from rest_framework.views import APIView
from comptes.permissions import ComptesPermissions

class UserCreate(APIView):
    serializer_class = UserSerializer
    permission_classes = [ComptesPermissions]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'user_id': user.id},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
