from django.shortcuts import get_object_or_404, render
from django.views import generic
from . import models, forms
from django.http import HttpResponse
from electronics.models import Electronics


class ElectronicsListView(generic.ListView):
    template_name = 'electronics/list.html'
    context_object_name = 'electronics_list'
    model = Electronics

    def get_queryset(self):
        return self.model.objects.filter().order_by("-id")


class OldAgeListView(generic.ListView):
    template_name = 'electronics/old_list.html'
    context_object_name = 'old'
    model = Electronics

    def get_queryset(self):
        return models.Electronics.objects.filter(tags__name='Пенсионеры').order_by('-id')


class YoungAgeListView(generic.ListView):
    template_name = 'electronics/young_list.html'
    context_object_name = 'young'
    models = Electronics

    def get_queryset(self):
        return models.Electronics.objects.filter(tags__name='Молодежь').order_by('-id')


class DetailElectronicsView(generic.DetailView):
    template_name = 'electronics/detail.html'
    context_object_name = 'electronic'

    def get_object(self, **kwargs):
        electronics_id = self.kwargs.get("id")
        return get_object_or_404(models.Electronics, id=electronics_id)


class SearchElectronicsView(generic.ListView):
    template_name = "electronics/list.html"
    context_object_name = "electronics_list"
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return models.Electronics.objects.filter(title__icontains=query).order_by(
                "name"
            )
        return models.Electronics.objects.all().order_by("name")


def create_comment_view(request):
    if request.method == "POST":
        form = forms.CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Ваш комментарий успешно добавлен</h1>")
    else:
        form = forms.CommentForm()

    return render(request, "electronics/create_comment.html", {"form": form})



