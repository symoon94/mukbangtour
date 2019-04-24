from django.urls import path
from . import views

urlpatterns =[
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.DetailView.as_view(), name='post_detail'),
    path('create/', views.post_new, name='post_new'),
    path('<int:pk>/update/', views.post_update, name='post_update'),
    path('draft/', views.post_draft, name='post_draft'),
    path('<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('<int:pk>/comment/', views.comment_new, name='comment_new'),
    path('<int:pk>/comment/approve', views.comment_approve, name='comment_approve'),
    path('<int:pk>/comment/remove', views.comment_remove, name='comment_remove')
]