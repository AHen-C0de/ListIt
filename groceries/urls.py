from django.urls import path

from groceries.views.grocery_view import GroceriesView

urlpatterns = [
    path('', GroceriesView.as_view(), name='groceries'),
]
