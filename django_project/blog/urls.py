from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    VacanciesListView,
    VacanciesDetailView,
    HrdocListView,
    Corp_docListView,
    AppsListView,
    FAQsListView)

urlpatterns = [
    path('home/', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('vacancies/', VacanciesListView.as_view(), name='vacancies-home'),
    path('vacancies/<int:pk>/', VacanciesDetailView.as_view(), name='vacancies-detail'),
    path('vacancies/apply/', views.create_application, name='post_application'),
    path('hr-forms/', HrdocListView.as_view(), name='hrdocs-home'),
    path('corporate-docs/', Corp_docListView.as_view(), name='corporate-docs'),
    path('company-apps/', AppsListView.as_view(), name='company-apps'),
    path('faqs/', FAQsListView.as_view(), name='faqs')


  
]
