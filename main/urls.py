from django.urls import path
from .views import project_list, create_icecream

urlpatterns = [
    path('', project_list, name='project_list'),
    path('icecream/', create_icecream, name='icecream'),
]