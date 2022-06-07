# from django.contrib.auth.models import Group, Permission
# from django.contrib.auth.validators import UnicodeUsernameValidator
# from django.contrib.contenttypes.models import ContentType
# from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
# from django.contrib.auth.password_validation import validate_password
# from .models import User, Role, UserInfo
# from .utils import get_user_permissions


# class PermissionSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Permission
#         fields = ['id', 'codename']


# class RoleSerializer(serializers.ModelSerializer):
#     permissions = Permission.objects.values('id')

#     class Meta:
#         model = Role
#         fields = ['id', 'name', 'description', 'permissions']


# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['id', 'name']


# class UserSerializer(serializers.ModelSerializer):
#     roles = GroupSerializer(source='groups', many=True, read_only=True)
#     permissions = serializers.SerializerMethodField(method_name='get_permissions')

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'section', 'position', 'full_name', 
#                     'date_of_birthday', 'gender','degree', 'inps_number', 
#                     'phone',  'roles', 'permissions')

#     def get_permissions(self, instance):
#         groups = instance.groups.all()
#         return get_user_permissions(groups)


# class RelatedUserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, allow_blank=True, required=False)

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'password')
#         extra_kwargs = {
#             'username': {
#                 'validators': [UnicodeUsernameValidator(), UniqueValidator(queryset=User.objects.all())],
#             }
#         }


# class RelatedUserPutSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, allow_blank=True, required=False)

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'password')
#         extra_kwargs = {
#             'username': {
#                 'validators': [],
#             }
#         }



# class ContentTypeSerializer(serializers.ModelSerializer):
#     permissions = serializers.SerializerMethodField(method_name='get_permissions')

#     class Meta:
#         model = ContentType
#         fields = ('id', 'model', 'permissions')

#     def to_representation(self, instance):
#         ret = super().to_representation(instance)
#         if hasattr(instance, 'extendedcontenttype'):
#             ret['model'] = instance.extendedcontenttype.extend_name.upper()
#         else:
#             ret['model'] = ret['model'].upper()
#         return ret

#     def get_permissions(self, instance):
#         permissions = Permission.objects.filter(content_type=instance.id)
#         result = []
#         for p in permissions:
#             result.append(
#                 {"id": p.id, "name": p.codename.split('_')[0].upper()}
#             )
#         return result


# # class UserPasswordChangeSerializer(serializers.Serializer):
# #     old_password = serializers.CharField(required=True)
# #     new_password = serializers.CharField(required=True)

# #     def validate_new_password(self, value):
# #         validate_password(value)
# #         return value

# # class UserSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = UserInfo
# #         fields = ['id', 'username', 'email', 'user_role', 'region_name', 'district_name']

# #     def update(self, instance, validated_data):
# #         for key, value in validated_data.items():
# #             setattr(instance, key, value)
# #         instance.save()
# #         return instance



# # class AppModuleSerializer(serializers.ModelSerializer):
# #     modules = ContentTypeSerializer(source='content_types', read_only=True, many=True)

# #     class Meta:
# #         model = AppModule
# #         fields = ('id', 'name', 'modules')
