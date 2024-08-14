from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('insert',views.insert),
    path('display',views.display),
    path('edit/<std>',views.edit),
    path('delete/<name>',views.delete),
]