#from django.shortcuts import render
from django.views.generic import TemplateView

class ShoppingListView(TemplateView):
    template_name='edit_list/shoppingList.html'