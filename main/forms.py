from django.forms import ModelForm
from .models import Project, IceCream


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title']


class IceCreamForm(ModelForm):
    class Meta:
        model = IceCream
        fields = ['name', 'flavor', 'price']