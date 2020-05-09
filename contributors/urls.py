from django.views import generic

from django.urls import path
from .views import (
            ContributorListView,
            CreateContributorView,
        )

app_name = 'contributors'
urlpatterns = [
    path('', generic.TemplateView.as_view(template_name='contributors/home.html'), name='home'),
    path('thank-you', generic.TemplateView.as_view(template_name='contributors/thank_you.html'), name='thank_you'),
    path('create-contributor', CreateContributorView.as_view(), name='create_contributor'),
    path('contributor-list', ContributorListView.as_view(), name='contributor_list'),
    path('contributor-list', ContributorListView.as_view(), name='contributor_list'),
]