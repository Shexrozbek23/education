import mimetypes
import os
import uuid
# import viewsets
from email.mime import application
from threading import stack_size
from rest_framework import viewsets
from django.http import Http404, JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import mixins, views, generics, viewsets, response, status, permissions
from rest_framework.views import APIView
from django.db.models import Q, Sum
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser, JSONParser
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, get_object_or_404
from rest_framework.response import Response
from .responses import nonContent
from django.contrib.auth.models import User
# import local data
from .serializers import *
from .models import PHenology,Photo,Production,Protect,Research,Note,Experiment
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from users.models import UserInfo
from rest_framework.pagination import LimitOffsetPagination
class UserView(APIView):

    def get(self, request):
        serializer = UserSerializer(request.user)
        return response.Response(serializer.data)

    def get_object(self, queryset=None):
        return self.request.user




class CountryList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountrySerializer
    pagination_class = None

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProductTypeList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = ProductTypes.objects.all()
    serializer_class = ProductTypeSerializer
    pagination_class = None

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MonthList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Months.objects.all()
    serializer_class = MonthSerializer
    pagination_class = None

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)





class PhenologyView(ListCreateAPIView):
    serializer_class = PhenologySerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)

    filterset_fields = ['created_by', 'updated_by']
    ordering = ['pk']

    def get_queryset(self):
        return PHenology.objects.all()

    def get(self, request, *args, **kwargs):
        self.serializer_class = PhenologySerializer
        return self.list(request, *args, **kwargs)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PhenologyUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = PhenologySerializer


    def get_queryset(self):
        return PHenology.objects.all()

    def get(self, request, pk):
        instance = get_object_or_404(PHenology, id=pk)
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        instance = get_object_or_404(PHenology, id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=self.request.user)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def delete(self, request, pk):
        instance = get_object_or_404(PHenology, id=pk)
        instance.delete()
        return Response(nonContent(), status.HTTP_204_NO_CONTENT)


class ProductView(ListCreateAPIView):
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)

    filterset_fields = ['created_by', 'updated_by']
    ordering = ['pk']

    def get_queryset(self):
        return Production.objects.all()

    def get(self, request, *args, **kwargs):
        self.serializer_class = ProductSerializer
        return self.list(request, *args, **kwargs)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class ProductUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer


    def get_queryset(self):
        return Production.objects.all()

    def get(self, request, pk):
        instance = get_object_or_404(Production, id=pk)
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        instance = get_object_or_404(Production, id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=self.request.user)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def delete(self, request, pk):
        instance = get_object_or_404(Production, id=pk)
        instance.delete()
        return Response(nonContent(), status.HTTP_204_NO_CONTENT)    



class ProtectionView(ListCreateAPIView):
    serializer_class = ProtectionSerializer

    def get_queryset(self):
        return Protect.objects.all()

    def get(self, request, *args, **kwargs):
        self.serializer_class = ProtectionSerializer
        return self.list(request, *args, **kwargs)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProtectionUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProtectionSerializer

    def get_queryset(self):
        return Protect.objects.all()

    def get(self, request, pk):
        instance = get_object_or_404(Protect, id=pk)
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        instance = get_object_or_404(Protect, id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=self.request.user)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def delete(self, request, pk):
        instance = get_object_or_404(Protect, id=pk)
        instance.delete()
        return Response(nonContent(), status.HTTP_204_NO_CONTENT)    




class ResearchU(ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_serializer_class(self):
        return ResearchSerializer

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        for f in self.request.data.getlist('photos'):
            mf = Photo.objects.create(photo=f, created_by=self.request.user)
            obj.photos.add(mf)
        # # 
        for n in self.request.data.getlist('notes'):
            mn = Note.objects.create(note=n, created_by=self.request.user)
            obj.notes.add(mn)

        for m in self.request.data.getlist('experiments'):
            bm = Experiment.objects.create(experiment=m, created_by=self.request.user)
            obj.experiments.add(bm)

        # for b in self.request.data.getlist('phenology'):
        #     bm = PHenology.objects.create(pheno_status=b, created_by=self.request.user)
        #     obj.phenology.add(bm)

    parser_classes = (MultiPartParser, JSONParser, )

    serializer_class = ResearchSerializer

    http_method_names = ['get','post','delete','put','patch', 'head']

    def get_queryset(self):
        return self.request.user.batches.all()

    # def get(self, request, pk):
    #     instance = get_object_or_404(Research, id=pk)
    #     serializer = self.serializer_class(instance)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        self.serializer_class = ResearchSerializer
        return self.list(request, *args, **kwargs)



    # def post(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(created_by=self.request.user)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


class ResearchUpdateU(RetrieveUpdateDestroyAPIView):
    serializer_class = ResearchSerializer

    def get_queryset(self):
        return Research.objects.all()


    def get(self, request, pk):
        instance = get_object_or_404(Research, id=pk)
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        instance = get_object_or_404(Research, id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=self.request.user)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def delete(self, request, pk):
        instance = get_object_or_404(Research, id=pk)
        instance.delete()
        return Response(nonContent(), status.HTTP_204_NO_CONTENT)

class ResearchDetailView(ListCreateAPIView):

    serializer_class = ResearchSerializer

    def get_queryset(self):
        return Research.objects.all()

    def get(self, request, *args, **kwargs):
        self.serializer_class = ResearchSerializer
        return self.list(request, *args, **kwargs)
    

class PhotoDownloadView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, pk):
        attachment = get_object_or_404(Photo, id=pk)
        file_extension = os.path.splitext(attachment.file.path)[1]
        file = open(attachment.file.path, 'rb')
        mime_type, _ = mimetypes.guess_type(attachment.file.path)
        response = HttpResponse(file, content_type=mime_type)
        response['Content-Disposition'] = 'attachment; filename="%s%s"' % (str(uuid.uuid4()), file_extension)
        return response

class NoteDownloadView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, pk):
        attachment = get_object_or_404(Note, id=pk)
        file_extension = os.path.splitext(attachment.file.path)[1]
        file = open(attachment.file.path, 'rb')
        mime_type, _ = mimetypes.guess_type(attachment.file.path)
        response = HttpResponse(file, content_type=mime_type)
        response['Content-Disposition'] = 'attachment; filename="%s%s"' % (str(uuid.uuid4()), file_extension)
        return response

class ExperimentDownloadView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, pk):
        attachment = get_object_or_404(Experiment, id=pk)
        file_extension = os.path.splitext(attachment.file.path)[1]
        file = open(attachment.file.path, 'rb')
        mime_type, _ = mimetypes.guess_type(attachment.file.path)
        response = HttpResponse(file, content_type=mime_type)
        response['Content-Disposition'] = 'attachment; filename="%s%s"' % (str(uuid.uuid4()), file_extension)
        return response




# class AttachmentPhotoVResearchDetailViewiew(ListCreateAPIView):
#     serializer_class = AttachmentPhotoSerializer
#     parser_classes = [MultiPartParser, FormParser, FileUploadParser, JSONParser]
#     pagination_class = None
#     ordering = ['-pk']

#     def get_queryset(self):
#         return AttachmentPhoto.objects.all()

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(created_by=self.request.user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

    

# class AttachmentPhotoDetailView(RetrieveUpdateDestroyAPIView):
#     serializer_class = AttachmentPhotoSerializer
#     http_method_names = ['get', 'put', 'delete']

#     def get(self, request, pk):
#         attachment = get_object_or_404(AttachmentPhoto, id=pk)
#         serializer = self.serializer_class(attachment)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         attachment = get_object_or_404(AttachmentPhoto, id=pk)
#         serializer = self.serializer_class(attachment, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(updated_by=self.request.user)
#         return Response(serializer.data, status.HTTP_202_ACCEPTED)

#     def delete(self, request, pk):
#         attachment = get_object_or_404(AttachmentPhoto, id=pk)
#         attachment.delete()
#         return Response(nonContent(), status.HTTP_204_NO_CONTENT)


# class AttachmentNoteView(ListCreateAPIView):
#     serializer_class = AttachmentNoteSerializer
#     parser_classes = [MultiPartParser, FormParser, FileUploadParser]
#     pagination_class = None
#     ordering = ['-pk']

#     def get_queryset(self):
#         return AttachNote.objects.all()

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(created_by=self.request.user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class AttachmentNoteDetailView(RetrieveUpdateDestroyAPIView):
#     serializer_class = AttachmentNoteSerializer
#     http_method_names = ['get', 'put', 'delete']

#     def get(self, request, pk):
#         attachment = get_object_or_404(AttachNote, id=pk)
#         serializer = self.serializer_class(attachment)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         attachment = get_object_or_404(AttachNote, id=pk)
#         serializer = self.serializer_class(attachment, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(updated_by=self.request.user)
#         return Response(serializer.data, status.HTTP_202_ACCEPTED)

#     def delete(self, request, pk):
#         attachment = get_object_or_404(AttachNote, id=pk)
#         attachment.delete()
#         return Response(nonContent(), status.HTTP_204_NO_CONTENT)


# class AttachmentExperimentView(ListCreateAPIView):
#     serializer_class = AttachmentExperimentSerializer
#     parser_classes = [MultiPartParser, FormParser, JSONParser, ]
#     pagination_class = None
#     ordering = ['-pk']

#     def get_queryset(self):
#         return AttachmentExperiment.objects.all()

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(created_by=self.request.user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class AttachmentExperimentDetailView(RetrieveUpdateDestroyAPIView):
#     serializer_class = AttachmentExperimentSerializer
#     http_method_names = ['get', 'put', 'delete']

#     def get(self, request, pk):
#         attachment = get_object_or_404(AttachmentExperiment, id=pk)
#         serializer = selffilter(id=1)
#     def put(self, request, pk):
#         attachment = get_object_or_404(AttachmentExperiment, id=pk)
#         serializer = self.serializer_class(attachment, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(updated_by=self.request.user)
#         return Response(serializer.data, status.HTTP_202_ACCEPTED)

#     def delete(self, request, pk):
#         attachment = get_object_or_404(AttachmentExperiment, id=pk)
#         attachment.delete()
#         return Response(nonContent(), status.HTTP_204_NO_CONTENT)

class WokrekResult(APIView):

    def get(self,request):
        context=[]
        s=1
        users = UserInfo.objects.all()
        for user in users:
            if user.user_role == 1:
                continue
            counts={}
            counts['user'] = user.full_name
            counts['Зарарлирганизм']=Research.objects.filter(created_by=user).count()
            counts['Маҳсулот']= Production.objects.filter(created_by=user).count()
            counts['Фенология']= PHenology.objects.filter(created_by=user).count()
            counts['Қаршикураш']= Production.objects.filter(created_by=user).count()
            counts['Фото']= Photo.objects.filter(created_by=user).count()
            counts['Қўлёзмалар']=Note.objects.filter(created_by=user).count()
            counts['Тажрибалар'] = Experiment.objects.filter(created_by=user).count()
            context.append(counts)
            s+=1
        return Response(context)

class Quarantine(APIView):

    def get(self,request):
        context={}
        karantin_true={}
        karantin_false={}
        karantin_all={}
        quarantine_type_true = Research.objects.filter(quarantine_type = '1')
        karantin_true['Karantinsoni'] = quarantine_type_true.count()
        karantin_true['Вирус'] = quarantine_type_true.filter(type='Вирус').count()
        karantin_true['Касаллик'] = quarantine_type_true.filter(type='Касаллик').count()
        karantin_true['Заракунанда'] = quarantine_type_true.filter(type='Заракунанда').count()
        karantin_true['Бегонаўт'] = quarantine_type_true.filter(type='Бегона ўт').count()
        karantin_true['Бактерия'] = quarantine_type_true.filter(type='Бактерия').count()
        context['Karantin']=karantin_true
        quarantine_type_false= Research.objects.filter(quarantine_type = '2')
        karantin_false['Karantinsoni'] = quarantine_type_false.count()
        karantin_false['Вирус'] = quarantine_type_false.filter(type='Вирус').count()
        karantin_false['Касаллик'] = quarantine_type_false.filter(type='Касаллик').count()
        karantin_false['Заракунанда'] = quarantine_type_false.filter(type='Заракунанда').count()
        karantin_false['Бегонаўт'] = quarantine_type_false.filter(type='Бегона ўт').count()
        karantin_false['Бактерия'] = quarantine_type_false.filter(type='Бактерия').count()
        context['Karantinemas']=karantin_false
        karantin_all['Organizm']= karantin_true['Karantinsoni']+karantin_false['Karantinsoni']
        karantin_all['Вирус'] = karantin_true['Вирус']+karantin_false['Вирус']
        karantin_all['Касаллик'] = karantin_true['Касаллик'] + karantin_false['Касаллик']
        karantin_all['Заракунанда'] = karantin_true['Заракунанда']+karantin_false['Заракунанда']
        karantin_all['Бегона'] =karantin_true['Бегонаўт'] + karantin_false['Бегонаўт']
        karantin_all['Бактерия'] = karantin_true['Бактерия'] + karantin_false['Бактерия']
        context['UmumiyKarantin'] = karantin_all
 
        print(quarantine_type_true.count())
        return Response(context)
        