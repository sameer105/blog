from django.urls import path
from .views import HomeView, DetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView

urlpatterns =[
    path('',HomeView.as_view(),name="home"),
    path('details/<int:pk>', DetailView.as_view(), name="details"),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('details/edit/<int:pk>',UpdatePostView.as_view(), name='update_post'),
    path('details/<int:pk>/remove',DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/',CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>',LikeView, name='like_post'),
    path('details/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]