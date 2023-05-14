from django.urls import path

from edit_list.views import ShoppingListView

urlpatterns = [
    path("", ShoppingListView.as_view(), name="shopping_list"),
]