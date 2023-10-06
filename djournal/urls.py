from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from submissions import views
from django.views.generic.base import RedirectView
from submissions.views import restrict_submissions

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home),
    path('submissions/', views.restrict_submissions, name='submissions'),
    path('search_submissions/', views.search_submissions, name='search_submissions'),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
]
