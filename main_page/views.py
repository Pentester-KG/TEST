from django.shortcuts import render
from . import models
from django.views import generic


class MainPageView(generic.ListView):
    template_name = 'electronics/main_page.html'
    context_object_name = 'main'
    ordering = ['-id']
    model = models.Deviz

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Deviz'] = models.Deviz.objects.order_by('id')
        context['TopTechnic'] = models.TopTechnics.objects.order_by('-id')
        context['Video'] = models.Video.objects.order_by('id')
        return context
