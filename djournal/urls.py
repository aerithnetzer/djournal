from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from submissions import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path('submissions/', views.submissions, name='submissions'),
    path('search_submissions/', views.search_submissions, name='search_submissions'),
    path('accounts/login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout_view'),
    path('submit/', views.upload_file, name='upload_file'),
    path('accounts/profile/', RedirectView.as_view(url='/submissions/')),
    path('my_submissions/', views.my_submissions, name='my_submissions'),
    path('accounts/create_account/', views.create_account, name='create_account'),
    path('edit/assign_reviewer/<int:submission_id>/', views.assign_reviewer, name='assign_reviewer'),
    path('review/review_submission/<int:submission_id>/', views.review_submission, name='review_submission'),
    ]
