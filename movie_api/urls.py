from django.urls import path

from . import views


urlpatterns = [
    path('', views.apiOverView, name='movie-api-overview'),
    path('register/', views.CustomUserCreate.as_view(), name='user-register'),
    path('logout/blacklist/', views.BlacklistTokenUpdateView.as_view(), name='blacklist'),
    path('users/', views.SysUserList.as_view(), name='users-list'),
    path('users/add/', views.SysUserCreate.as_view(), name='users-add'),
    path('user/<int:pk>/detail/',views.SysUserDetail.as_view(), name='user-detail'),
    path('movies/', views.MovieList.as_view(), name='movies-list'),
    path('category/<str:cat>/', views.moviesCategory, name='movie-category'),
    path('movies/add/', views.MovieCreate.as_view(), name='movies-add'),
    path('movie/<int:id>/detail/', views.MovieDetail.as_view(), name='movie-detail'),
    path('comments/', views.CommentList.as_view(), name='comments'),
    path('comments/add/', views.CommentCreate.as_view(), name='comments-add'),
    path('comment/<int:id>/detail/', views.CommentDetail.as_view(), name='comment-detail')
]
