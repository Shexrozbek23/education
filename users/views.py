# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.response import Response
# from rest_framework.views import APIView

# # from restapp.pagination import ResultsSetPagination
# from .models import Role
# from .serializers import UserSerializer, RoleSerializer


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
