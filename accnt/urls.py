# myapp/urls.py


from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView

urlpatterns = [
                  path('', views.index, name='index'),
                  path('my_login/', views.my_login, name='my_login'),
                  path('house_help_list/', views.house_help_list, name='house_help_list'),
                  path('house_help_registration/', views.house_help_registration, name='house-registration'),
                  path('house_employer_registration/', views.house_employer_registration,
                       name='house_employer_registration'),
                  path('employer_list/', views.employer_list, name='employer_list'),
                  path('profile/', views.profile, name='profile'),
                  path('register/', RegisterView.as_view(), name='register'),
                  path('login/', auth_views.LoginView.as_view(template_name='accnt/my_login.html'), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
