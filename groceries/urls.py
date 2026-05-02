from django.urls import include, path
from rest_framework.routers import SimpleRouter
from groceries.views.api.item_viewset import ItemViewset
from groceries.views.grocery_view import GroceriesView
from . import apps


app_name = apps.GroceriesConfig.name


router = SimpleRouter()
router.register(
    r"items", ItemViewset, basename="items"
)

urlpatterns = [
    path('', GroceriesView.as_view(), name=app_name),
    path('', include(router.urls))
]
