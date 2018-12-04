from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,FormView,DeleteView,UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy,reverse

from . models import Add_story
from .forms import PostForm
# Create your views here.

class IndexView(ListView):
    template_name="diary/default.html"
    context_object_name='diarys'
    def get_queryset(self):
      return Add_story.objects.all()

class MyFormView(FormView):
    form_class=PostForm
    template_name="diary/form.html"
    success_url='/diary/'
    def form_valid(self,form):
        diary = form.save(commit = False)
        diary.generate()
        return super().form_valid(form)

class UpdateView(UpdateView):
    model = Add_story
    fields =['title','content','update_date']
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('detail', args = (self.object.id,))

class DeleteView(DeleteView):
    model= Add_story
    template_name="diary/detail.html"
    success_url = reverse_lazy('index')


class DetailView(DetailView):
    model=Add_story
    template_name="diary/detail.html"
    context_object_name = 'diary'


class CreateUserView(CreateView):
    template_name = 'registration/signup.html'

    form_class = UserCreationForm
    success_url = reverse_lazy('create_user_done')

class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'
