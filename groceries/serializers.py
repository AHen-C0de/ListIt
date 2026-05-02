from rest_framework.serializers import ModelSerializer

from groceries.models import Item


class ItemSerializer(ModelSerializer):

    class Meta:
        model = Item
        fields = ("name",)
