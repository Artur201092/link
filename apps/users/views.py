from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.serializers import SignUpSerializer


class SignUpAPIView(APIView):

    serializer_class = SignUpSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Successfully created", status=status.HTTP_201_CREATED)
