from django.urls import path

from groceries.views import GroceriesView

urlpatterns = [
    path('', GroceriesView.as_view(), name='groceries'),
]
