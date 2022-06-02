from django.conf import settings
from django.contrib.contenttypes.models import ContentType, ContentTypeManager
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, GroupManager
from django.utils.translation import gettext_lazy as _



GENDERS = (
    ('male', _('Male')),
    ('female', _('Female')),
)


class UserRoles(models.IntegerChoices):
    ADMIN = 1, 'ADMIN'
    WORKER = 2, 'WORKER'


class UserInfo(AbstractUser):
    section = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    full_name = models.CharField(max_length=400,null=True)
    date_of_birthday = models.CharField(max_length=50,default='',null=True)
    gender = models.CharField(choices=GENDERS, max_length=6, null=True, blank=True, )
    degree = models.CharField(max_length=255, null=True, blank=True)
    inps_number = models.CharField(null=True,default=0,max_length=60)
    phone_number = models.CharField(max_length=250,default='')
    user_role = models.IntegerField(choices=UserRoles.choices,default=2,null=True)
    status = models.BooleanField(default=True)
    # section = models.CharField(max_length=255, null=True, blank=True)
    # position = models.CharField(max_length=255, null=True, blank=True)
    # full_name = models.ForeignKey(User, max_length=30, blank=True, on_delete=models.SET_NULL, null=True)
    # date_of_birthday = models.DateField(_('date of birthday'), null=True, blank=True, )
    # gender = models.CharField(choices=GENDERS, max_length=6, null=True, blank=True, )
    # degree = models.CharField(max_length=255, null=True, blank=True)
    # inps_number = models.IntegerField(null=True, blank=True)
    # phone = models.IntegerField(null=True, blank=True)
    # username = models.CharField(max_length=255, null=False, blank=False, unique=True)
    # is_active = models.BooleanField(_('Active'), default=True)
    # avatar = models.ImageField(null=True)
    # created_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    # updated_by = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_by_user', null=True, on_delete=models.SET_NULL)
    # updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='updated_by_user', null=True, on_delete=models.SET_NULL)

    # USERNAME_FIELD = 'phone'
    # objects = UserManager()
    # REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f'{self.full_name}'


# class Role(Group):
#     objects = GroupManager()

#     description = models.CharField(max_length=255)

#     class Meta:
#         verbose_name = _('role')
#         verbose_name_plural = _('roles')

