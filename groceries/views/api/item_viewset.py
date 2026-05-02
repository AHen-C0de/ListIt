from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from groceries.models import Item
from groceries.serializers import ItemSerializer


class ItemViewset(ListModelMixin, GenericViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
