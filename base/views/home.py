from typing import Any
from django.views.generic import TemplateView
from base.apps_config import app_configs

class HomeView(TemplateView):
    template_name='base/home.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["apps"] = app_configs
        return context
