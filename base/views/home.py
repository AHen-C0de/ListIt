from django.views.generic import TemplateView

from base.models import List

class HomeView(TemplateView):
    template_name='base/home.html'
