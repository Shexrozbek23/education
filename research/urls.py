from django.urls import path, include, re_path
# import routers
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from .views import *

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used

app_name = 'research'

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    # Phenology urls
    re_path(r"^phenology/$", PhenologyView.as_view(), name='phenology view'),
    path("phenology/<pk>", PhenologyUpdateView.as_view(), name='update phenology view'),
    #  Product urls
    re_path(r"^product/$", ProductView.as_view(), name='product view'),
    path("product/<pk>", ProductUpdateView.as_view(), name='update product view'),
    #  Protection urls
    re_path(r"^protection/$", ProtectionView.as_view(), name='protection view'),
    path("protection/<pk>", ProtectionUpdateView.as_view(), name='update protection view'),
    re_path(r"^researchall/$", ResearchDetailView.as_view(), name='research view'),
    re_path(r"^research/$", ResearchU.as_view(), name='research view'),
    path("research/<pk>", ResearchUpdateU.as_view(), name='research update view'),
    re_path(r"^country/$", CountryList.as_view(), name='country view'),
    re_path(r"^productypes/$", ProductTypeList.as_view(), name='productype view'),
    re_path(r"^months/$", MonthList.as_view(), name='Months'),
    re_path(r'^auth/$', auth_views.obtain_auth_token),
    path('photodown/<int:pk>', PhotoDownloadView.as_view(), name='photo_download'),
    path('notedown/<int:pk>', NoteDownloadView.as_view(), name='note_download'),
    path('experimentdown/<int:pk>', ExperimentDownloadView.as_view(), name='experiment_download'),
    re_path(r"^worker/result/$", WokrekResult.as_view()),
    re_path(r"^quarantine/result/$", Quarantine.as_view()),
    re_path(r'^user/change/password$',UserPasswordChangeAPIView.as_view()),
    re_path(r'^plants$',PlantAPIView.as_view())
]
