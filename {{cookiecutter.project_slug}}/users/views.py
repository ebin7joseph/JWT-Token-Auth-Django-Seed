from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import UserRegistrationSerializer
from .serializers import UserLoginSerializer, UserDetailSerializer
from .models import UserProfile


class UserRegistrationView(CreateAPIView):

    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            "success": True,
            "status code": status.HTTP_200_OK,
            "message": "User registered successfully",
        }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)


class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            "success": True,
            "status code": status.HTTP_200_OK,
            "email": serializer.data["email"],
            "message": "User logged in successfully",
            "token": serializer.data["token"],
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)


class UserView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserDetailSerializer

    def get(self, request, email):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data)


class UserProfileView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            status_code = status.HTTP_200_OK
            response = {
                "success": True,
                "status code": status_code,
                "message": "User profile fetched successfully",
                "data": [
                    {
                        "name": user_profile.name,
                    }
                ],
            }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                "success": False,
                "status code": status.HTTP_400_BAD_REQUEST,
                "message": "User does not exists",
                "error": str(e),
            }
        return Response(response, status=status_code)
