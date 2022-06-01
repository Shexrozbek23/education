# import serializer from rest_framework
from pyexpat import model
from django.shortcuts import get_object_or_404
from pkg_resources import require
from rest_framework import serializers
from django.contrib.auth.models import User

import research
# import model from models.py
from .models import *
from django import forms
from drf_writable_nested.serializers import WritableNestedModelSerializer



class CountryRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, name_ru):
        return str(name_ru)

    def to_internal_value(self, data):
        return Countries.objects.get(id=data)

class MonthRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, month):
        return str(month)

    def to_internal_value(self, data):
        return Months.objects.get(id=data)

class ProductRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, product):
        return str(product)

    def to_internal_value(self, data):
        return ProductTypes.objects.get(id=data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = '__all__'


class ProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductTypes
        fields = '__all__'


class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Months
        fields = '__all__'





class PhenologySerializer(serializers.ModelSerializer):
   
    pheno_status = serializers.BooleanField(required=False, default=False)
    created_by = serializers.SerializerMethodField(method_name='get_created_user_name', read_only=True)
    updated_by = serializers.SerializerMethodField(method_name='get_updated_user_name', read_only=True)
    month_eggs = MonthRelatedField(queryset=Months.objects.all(), many=True, required=False)
    month_larva = MonthRelatedField(queryset=Months.objects.all(), many=True, required=False)
    month_fungus = MonthRelatedField(queryset=Months.objects.all(), many=True, required=False)
    month_mature = MonthRelatedField(queryset=Months.objects.all(), many=True, required=False)
    month_m = MonthRelatedField(queryset=Months.objects.all(), many=True, required=False)

    class Meta:
        model = PHenology
        fields = ('id', 'pheno_status',
                  'eggs', 'month_eggs', 'day_eggs', 'larva', 'month_larva', 'day_larva', 'fungus',
                  'month_fungus', 'day_fungus', 'mature', 'month_mature', 'day_mature', 'manipulation',
                  'month_m', 'day_m', 'prediction', 'created_by', 'updated_by')

    def get_created_user_name(self, instance):
        return instance.created_by.username if instance.created_by else None

    def get_updated_user_name(self, instance):
        return instance.updated_by.username if instance.updated_by else None


class ProductSerializer(serializers.ModelSerializer):
    # specify model and fields
    created_by = serializers.SerializerMethodField(method_name='get_created_user_name', read_only=True)
    updated_by = serializers.SerializerMethodField(method_name='get_updated_user_name', read_only=True)
    type_product = ProductRelatedField(queryset=ProductTypes.objects.all(), many=True, required=False)
    product_status = serializers.BooleanField(required=False, default=False)

    
    class Meta:
        model = Production
        fields = ('id', 'product_status', 'product', 'product_hs_code', 'type_product', 'created_by', 'updated_by')

    def get_created_user_name(self, instance):
        return instance.created_by.username if instance.created_by else None

    def get_updated_user_name(self, instance):
        return instance.updated_by.username if instance.updated_by else None


class ProtectionSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField(method_name='get_created_user_name', read_only=True)
    updated_by = serializers.SerializerMethodField(method_name='get_updated_user_name', read_only=True)
    protect_status = serializers.BooleanField(required=False, default=False)


    # specify model and fields
    class Meta:
        model = Protect
        fields = ('id', 
                  'protect_status', 'agro_protect', 'bio_protect', 'chemistry_protect', 'created_by', 'updated_by')

    def get_created_user_name(self, instance):
        return instance.created_by.username if instance.created_by else None

    def get_updated_user_name(self, instance):
        return instance.updated_by.username if instance.updated_by else None




class PhotoSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField(method_name='get_created_user_name', read_only=True)
    updated_by = serializers.SerializerMethodField(method_name='get_updated_user_name', read_only=True)
    photo = serializers.FileField(required=False)
    research = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Photo
        fields = ('id', 'photo', 'photos', 'created_by', 'updated_by', 'research')

    def get_created_user_name(self, instance):
        return instance.created_by.username if instance.created_by else None

    def get_updated_user_name(self, instance):
        return instance.updated_by.username if instance.updated_by else None


        

class NoteSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField(method_name='get_created_user_name', read_only=True)
    updated_by = serializers.SerializerMethodField(method_name='get_updated_user_name', read_only=True)


    class Meta:
        model = Note
        fields = '__all__'

    def get_created_user_name(self, instance):
        return instance.created_by.username if instance.created_by else None

    def get_updated_user_name(self, instance):
        return instance.updated_by.username if instance.updated_by else None


class ExperimentSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField(method_name='get_created_user_name', read_only=True)
    updated_by = serializers.SerializerMethodField(method_name='get_updated_user_name', read_only=True)


    class Meta:
        model = Experiment
        fields = '__all__'

    def get_created_user_name(self, instance):
        return instance.created_by.username if instance.created_by else None

    def get_updated_user_name(self, instance):
        return instance.updated_by.username if instance.updated_by else None



class ResearchSerializer(WritableNestedModelSerializer):
   
    country = CountryRelatedField(queryset=Countries.objects.all(), many=True, required=False)
    phenology = PhenologySerializer(many=True, read_only=True)
    product = ProductSerializer(many=True, read_only=True)
    protection = ProtectionSerializer(many=True, read_only=True)
    photos = PhotoSerializer(many=True, required=False)
    notes = NoteSerializer(many=True, required = False)
    experiments = ExperimentSerializer(many=True, required=False)
    created_by = serializers.SerializerMethodField(method_name='get_created_user_name', read_only=True)
    updated_by = serializers.SerializerMethodField(method_name='get_updated_user_name', read_only=True)

    class Meta:
        model = Research
        fields =  '__all__'
    

    def get_created_user_name(self, instance):
        return instance.created_by.username if instance.created_by else None

    def get_updated_user_name(self, instance):
        return instance.updated_by.username if instance.updated_by else None









