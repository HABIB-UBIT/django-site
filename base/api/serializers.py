### Serializers are classes which turn python object into a Json data of the particular model or object

from rest_framework.serializers import ModelSerializer
from base.models import *

class RoomSerializer(ModelSerializer):
    class Meta:
        model= Room
        fields= '__all__'
