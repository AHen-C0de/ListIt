from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.filters import SearchFilter

from groceries.models import Item
from groceries.serializers import ItemSerializer


class ItemViewset(ListModelMixin, UpdateModelMixin, GenericViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name"] #* the name of the query_param must be `SearchFilter.search_param` ("search")
