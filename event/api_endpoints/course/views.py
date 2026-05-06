from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from account.permissions import IsTeacherUserRole, IsAdminUserRole
from drf_yasg.utils import swagger_auto_schema

from event.api_endpoints.course.serializer import LessonSerializer, CourseSerializer
from event.models import Course, Lesson


class CourseListAPIView(APIView):
    permission_classes = []

    @swagger_auto_schema(responses={200: CourseSerializer}, tags=['course'])
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True )
        return Response(serializer.data)
    

class CourseAPIView(APIView):
    permission_classes = [IsTeacherUserRole]

    @swagger_auto_schema(responses={200: CourseSerializer}, tags=['course'])
    def get(self, request):
        course = Course.objects.filter(owner=request.user).first()
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    
    @swagger_auto_schema(request_body=CourseSerializer, tags=['course'])
    def post(self, request):
        serializer = CourseSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class CourseDetailAPIView(APIView):
    permission_classes = [IsTeacherUserRole]

    @swagger_auto_schema(responses={200: CourseSerializer}, tags=['course'])
    def get(self, request, pk):
        course = Course.objects.filter(owner=request.user, pk=pk).first()

        if not course:
            return Response({'detail': 'Bunday id da Course topilmadi.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    

    @swagger_auto_schema(request_body=CourseSerializer, tags=['course'])
    def put(self, request, pk):
        course = Course.objects.filter(owner=request.user, pk=pk).first()
        serializer = CourseSerializer(course, data=request.data, context={'request': request})

        if not course:
            return Response({'detail': 'BUnday id da Course topilmadi.'}, status=status.HTTP_404_NOT_FOUND)
        

        if serializer.is_valid(raise_exception=True):
            serializer.save(owner=request.user)
            return Response(serializer.data)
        

    @swagger_auto_schema(responses={200: CourseSerializer}, tags=['course'])
    def delete(self, request, pk):
        course = Course.objects.filter(owner=request.user, pk=pk).first()

        if not course:
            return Response({'detail': 'Bunday id da Course topilmadi.'}, 
                status=status.HTTP_404_NOT_FOUND)
        
        course.delete()
        return Response({'detail': 'Course muvaffaqiyatli uchirildi!'})
    


class LessonListAPIView(APIView):
    permission_classes = []

    @swagger_auto_schema(responses={200: LessonSerializer(many=True)}, tags=['lesson'])
    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)


class LessonAPIView(APIView):
    permission_classes = [IsTeacherUserRole]


    @swagger_auto_schema(responses={200: LessonSerializer(many=True)}, tags=['lesson'])
    def get(self, request):
        lessons = Lesson.objects.filter(owner=request.user)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)
    

    @swagger_auto_schema(request_body=LessonSerializer, tags=['lesson'])
    def post(self, request):
        serializer = LessonSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            course_id = request.data.get('course')
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class LessonDetailAPIView(APIView):
    permission_classes = [IsTeacherUserRole]

    def get_object(self, pk, user):
        return Lesson.objects.filter(owner=user, pk=pk).first()


    @swagger_auto_schema(responses={200: LessonSerializer}, tags=['lesson'])
    def get(self, request, pk):
        lesson = self.get_object(pk, request.user)
        if not lesson:
            return Response({'detail': 'Dars topilmadi.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)
    

    @swagger_auto_schema(request_body=LessonSerializer, tags=['lesson'])
    def put(self, request, pk):
        lesson = self.get_object(pk, request.user)
        if not lesson:
            return Response({'detail': 'Dars topilmadi.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LessonSerializer(lesson, data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save(owner=request.user)
            return Response(serializer.data)
        

    @swagger_auto_schema(responses={204: "O'chirildi"}, tags=['lesson'])
    def delete(self, request, pk):
        lesson = self.get_object(pk, request.user)
        if not lesson:
            return Response({'detail': 'Dars topilmadi.'}, status=status.HTTP_404_NOT_FOUND)
        
        lesson.delete()
        return Response({'detail': 'Dars muvaffaqiyatli o‘chirildi!'}, status=status.HTTP_200_OK)