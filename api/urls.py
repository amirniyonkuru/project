from django.urls import path
from . import views


urlpatterns = [
    path("categories/<slug:slug>/", views.category, name="categories"),
]