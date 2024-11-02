from rest_framework.viewsets import ModelViewSet

# Create your views here.
from materials.models import Course
from materials.serializer import CourseSerializer


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


# Create your views here.
