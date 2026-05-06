from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.permissions import IsAdminUserRole
from drf_yasg.utils import swagger_auto_schema

from event.api_endpoints.category.serializer import CategorySerializer, SubCategorySerializer
from event.models import Category, SubCategory


class CategoriyListAPIView(APIView):
    permission_classes = []

    @swagger_auto_schema(responses={200: CategorySerializer}, tags=['category'])
    def get(self, request):
        category = Category.objects.all()
        serialzer = CategorySerializer(category, many=True)
        return Response(serialzer.data)
    

class CategoryAPIVIew(APIView):
    permission_classes = [IsAdminUserRole]

    @swagger_auto_schema(responses={200: CategorySerializer}, tags=['category'])
    def get(self, request):
        category = Category.objects.filter(owner=request.user).first()
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    

    @swagger_auto_schema(request_body=CategorySerializer, tags=['category'])
    def post(self, request):
        serializer = CategorySerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        


class CategoryDetailAPIView(APIView):
    permission_classes = [IsAdminUserRole]

    @swagger_auto_schema(responses={200: CategorySerializer}, tags=['category'])
    def get(self, request, pk):
        category = Category.objects.filter(owner=request.user, pk=pk).first()

        if not category:
            return Response({'detail': 'Bunday id da kategoriya topilmadi.'}, 
                status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    

    @swagger_auto_schema(request_body=CategorySerializer, tags=['category'])
    def put(self, request, pk):
        category = Category.objects.filter(owner=request.user, pk=pk).first
        serializer = CategorySerializer(category, data=request.data, context={'request': request})

        if not category:
            return Response({'detail': 'Bunday id da kategoriya topilmadi.'}, 
                status=status.HTTP_404_NOT_FOUND)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

    @swagger_auto_schema(responses={200: CategorySerializer}, tags=['category'])
    def delete(self, request, pk):
        category = Category.objects.filter(owner=request.user, pk=pk).first()

        if not category:
            return Response({'detail': 'Bunday id da kategoriya topilmadi.'}, 
                status=status.HTTP_404_NOT_FOUND)
        
        category.delete()
        return Response({'detail': 'Category muvaffaqiyatli uchirildi!'})
    



class SubcategoryListAPIView(APIView):
    permission_classes = []

    @swagger_auto_schema(responses={200: SubCategorySerializer}, tags=['subcategory'])
    def get(self, request):
        category = SubCategory.objects.all()
        serializer = SubCategorySerializer(category, many=True)
        return Response(serializer.data)
    

class SubcategoryAPIView(APIView):
    permission_classes = [IsAdminUserRole]

    @swagger_auto_schema(responses={200: SubCategorySerializer}, tags=['subcategory'])
    def get(self, request):
        category = SubCategory.objects.filter(owner=request.user).first()
        serializer = SubCategorySerializer(category)
        return Response(serializer.data)
    
    
    @swagger_auto_schema(request_body=SubCategorySerializer, tags=['subcategory'])
    def post(self, request):
        serializer = SubCategorySerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        


class SubCategoryDetailAPIView(APIView):
    permission_classes = [IsAdminUserRole]

    @swagger_auto_schema(responses={200: SubCategorySerializer}, tags=['subcategory'])
    def get(self, request, pk):
        category = SubCategory.objects.filter(owner=request.user, pk=pk).first()

        if not category:
            return Response({'detail': 'BUnday id da SubCategoriya topilmadi.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SubCategorySerializer(category)
        return Response(serializer.data)
    

    @swagger_auto_schema(request_body=SubCategorySerializer, tags=['subcategory'])
    def put(self, request, pk):
        category = SubCategory.objects.filter(owner=request.user, pk=pk).first()
        serializer = SubCategorySerializer(category, data=request.data, context={'request': request})

        if not category:
            return Response({'detail': 'Bunday id da subcategoriya topilmadi.'}, 
                status=status.HTTP_404_NOT_FOUND)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

    @swagger_auto_schema(responses={200: SubCategorySerializer}, tags=['subcategory'])
    def delete(self, request, pk):
        category = SubCategory.objects.filter(owner=request.user, pk=pk).first()

        if not category:
            return Response({'detail': 'Bunday id da subcategoriya topilmadi.'}, 
                status=status.HTTP_404_NOT_FOUND)
        
        category.delete()
        return Response({'detail': 'SubCategory muvaffaqiyatli uchirildi!'})