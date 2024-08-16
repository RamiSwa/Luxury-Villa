from .models import Property
from .serializers import PropertySerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView


class PropertyApiList(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    


class PropertyApiDetail(RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    