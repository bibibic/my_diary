from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,FormView,DeleteView,UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.conf import settings
from django.contrib.auth import logout
from hitcount.views import HitCountDetailView


from . models import Add_story
from .forms import PostForm
# Create your views here.

'''class IndexView(ListView):
    template_name="diary/default.html"
    context_object_name='diarys'
    def get_queryset(self):
      return Add_story.objects.all()''' 
def Index(request):
    diarys=Add_story.objects.all()
    context={'diarys':diarys}
    return render(request,'diary/default.html',context)


class MyFormView(LoginRequiredMixin, FormView):
    login_url = '/accounts/login/'
    redirect_field_name = ''
    form_class=PostForm
    template_name="diary/form.html"
    success_url='/diary/'

    def form_valid(self,form):
        diary = form.save(commit = False)
        diary.auther = self.request.user
        diary.generate()
        return super().form_valid(form)

class UpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = ''
    model = Add_story
    fields =['title','content','update_date','image']
    template_name_suffix = '_update_form'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.auther != self.request.user:
            return HttpResponse("You are not allowed to edit this Post")
        return super(UpdateView, self).dispatch(request, *args, **kwargs)
    def get_success_url(self):
        return reverse_lazy('detail', args = (self.object.id,))




class DeleteView(LoginRequiredMixin, DeleteView):

    login_url = '/accounts/login/'
    redirect_field_name = ''
    model= Add_story
    template_name="diary/detail.html"
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.auther != self.request.user:
            return HttpResponse("You are not allowed to delete this Post")
        return super(DeleteView, self).dispatch(request, *args, **kwargs)
    success_url = reverse_lazy('index')


class DetailView(HitCountDetailView, DetailView):
    model=Add_story
    template_name="diary/detail.html"
    context_object_name = 'diary'
    count_hit = True


class CreateUserView(CreateView):
    template_name = 'registration/signup.html'

    form_class = UserCreationForm
    success_url = reverse_lazy('create_user_done')

class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'
