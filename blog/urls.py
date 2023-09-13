from . import views
from django.urls import path
from django.contrib.auth import views as auth_views 
# Add URLConf
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('register/', auth_views.RegisterView.as_view(form_class=UserCreationForm, template_name='registration/register.html'), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
]