from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("new", views.new, name="new"),
    path("delete/<int:tweet_id>/", views.delete, name="delete"),
    path("update/<int:tweet_id>/", views.update, name="update"),
]
