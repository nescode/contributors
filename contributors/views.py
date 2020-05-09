from django.shortcuts import render, redirect
from .forms import ContributeForm
from .models import CreateContributor
from django.views.generic.list import ListView
from django.views.generic import View
from django.views.generic.detail import DetailView


class CreateContributorView(View):
    def post(self, *args, **kwargs):
        if self.request.method == "POST":
            form = ContributeForm(self.request.POST or None, self.request.FILES or None)
            if form.is_valid():
                contributor_object = CreateContributor(name=form.cleaned_data['name'],
                                                       email=form.cleaned_data['email'],
                                                       phone=form.cleaned_data['phone'],
                                                       role=form.cleaned_data['role'],
                                                       resume=form.cleaned_data['resume'],
                                                       profession=form.cleaned_data['profession'],
                                                       about=form.cleaned_data['about']
                                                       )
                contributor_object.save()
                return redirect('/thank-you')

    def get(self, *args, **kwargs):
        context = {
            'form': ContributeForm()
        }
        return render(self.request, 'contributors/create_contributor.html', context)


class ContributorListView(ListView):
    model = CreateContributor
    paginate_by = 4
    template_name = 'contributors/contributor_list.html'
