# from django.contrib.auth.base_user import BaseUserManager
#
#
# class UserManager(BaseUserManager):
#     def create_user(self, username, password, phone):
#         user = self.model(username=username,
#                           fullname='User from terminal',
#                           phone=phone)  # new user with username
#         user.set_password(raw_password=password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, password, phone):
#         user = self.create_user(
#             username=username,
#             password=password,
#             phone=phone)
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
