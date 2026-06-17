from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Project
from .forms import IceCreamForm


def project_list(request):
    projects = Project.objects.all()

    paginator = Paginator(projects, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'main/project_list.html',
        {'page_obj': page_obj}
    )


def create_icecream(request):
    if request.method == 'POST':
        form = IceCreamForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = IceCreamForm()

    return render(
        request,
        'main/icecream_form.html',
        {'form': form}
    )