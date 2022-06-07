from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import response
from rest_framework import views
from rest_framework import permissions
# from restapp.pagination import ResultsSetPagination
# from .models import Role
from .serializers import UserPasswordChangeSerializer,UserSerializer
from rest_framework import status


class UserPasswordChangeAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return response.Response(serializer.data)

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request):
        self.object = self.get_object()
        serializer = UserPasswordChangeSerializer(data=request.data)
        user_info_serializer = UserSerializer(request.user)
        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return response.Response(
                    {
                        "old_password": ["Wrong password."]
                    },
                    status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return response.Response(user_info_serializer.data, status=status.HTTP_200_OK)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

























# class UserView(APIView):

#     def get(self, request):
#         user = request.user
#         serializer = UserSerializer(user)
#         return Response(serializer.data)


# class RoleView(ListCreateAPIView):
#     serializer_class = RoleSerializer

#     def get_queryset(self):
#         return Role.objects.all()

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, 201)


# class RoleDetailView(RetrieveUpdateDestroyAPIView):
#     serializer_class = RoleSerializer

#     def get_queryset(self):
#         return Role.objects.all()


# # class RolePermissionGridView(APIView):

# #     def get(self, request):
# #         modules = AppModule.objects.filter(on_dashboard=True)
# #         serializer = AppModuleSerializer(modules, many=True)

# #         return Response(serializer.data)
