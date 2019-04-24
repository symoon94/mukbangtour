
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/login/$', views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    url(r'^accounts/logout/$', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('board.urls')),
    url(r'^', include('favicon.urls')),
]
