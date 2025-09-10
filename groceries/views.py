from django.views.generic import ListView

from base.models import Item

class GroceriesView(ListView):
    template_name='groceries/groceries.html'
    model = Item
    context_object_name = "items"
