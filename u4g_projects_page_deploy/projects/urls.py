from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('', views.index, name = "all-projects"), #our-domain.com/projects
    path('request-success', views.request_success, name = "request-success"),
    path('request-project', views.request_project, name = "request-project"),
    path('ascezell/', views.company_profile, name = "ascezell"),
    path('collaborations/', views.collaborations, name = "collaborations"),
    path('collabtable', views.collabtable, name = "collabtable"),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('signup/login/', auth_views.LoginView.as_view(template_name='projects/login.html', authentication_form=LoginForm), name='login'),
    path('/<slug:project_slug>', views.project_details, name = "project-detail"), #our-domain.com/projects/a-second-project <dynamic-path-segment>
    path('<slug:project_slug>/success', views.confirm_registration, name = "confirm-registration"),
]