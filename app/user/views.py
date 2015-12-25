# Create your views here.
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'user/timeline/time_line.html'


IndexView = Index.as_view()
