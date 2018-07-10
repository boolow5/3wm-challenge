from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("sites", views.index, name="sites"),
    path("sites/<int:pk>", views.site_detail, name="site_details"),
    path("summary", views.summary, name="summary"),
    path("summary-average", views.summary_average, name="summary_average"),
]