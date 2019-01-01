"""my_diary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from diary import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('diary/',views.IndexView.as_view(), name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('diary/new/',views.MyFormView.as_view(),name="new_diary"),
    path('diary/<int:pk>/detail/',views.DetailView.as_view(),name="detail"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/',views.CreateUserView.as_view(),name='signup'),
    path('accounts/signup/done/',views.RegisteredView.as_view() ,name='create_user_done'),
    path('diary/<int:pk>/add_story_update_form/',views.UpdateView.as_view(), name='update'),
    path('diary/<int:pk>/delete/',views.DeleteView.as_view(), name='delete'),
    path('', TemplateView.as_view(template_name='logged_out.html'), name='logout'),
    ...

]
