from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_confirm_delete, name='tweet_confirm_delete'),
    path('<int:tweet_id>/like/', views.tweet_like_toggle, name='tweet_like_toggle'),

    path('register/', views.register, name='register'),
    path('user/<str:username>/', views.user_profile, name='user_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),

    path('<int:tweet_id>/comments/', views.comments_view, name='comments_view'),
    path('<int:tweet_id>/comments/add/', views.comment_add, name='comment_add'),
    path('comments/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
]
